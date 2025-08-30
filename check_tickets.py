import os
import sys
import json
import time
import logging
import contextlib
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# CONFIG
CONFIG_FILE = Path(__file__).parent / "config.json"
ALERTS_FILE = Path(__file__).parent / "alerts_sent.json"

# Load config
with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

MOVIE_NAME = config["movie_name"].strip()
TARGET_DATE = config["date"].strip()
THEATRES = config["theatres"]
HEADLESS = config.get("headless", False)

# Twilio creds from env vars
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

# Validate env vars
missing = [
    k for k, v in {
        "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
        "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
        "TWILIO_FROM": TWILIO_FROM,
        "TWILIO_TO": TWILIO_TO,
    }.items() if not v
]
if missing:
    raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# STATE STORAGE
if ALERTS_FILE.exists():
    with open(ALERTS_FILE, "r") as f:
        alerts_sent = set(json.load(f))
else:
    alerts_sent = set()

def save_alerts():
    with open(ALERTS_FILE, "w") as f:
        json.dump(sorted(list(alerts_sent)), f)

# SMS SENDER
def send_sms(movie, theatre_slug, show_date):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    body = f"🎉 Tickets for '{movie}' are LIVE at {theatre_slug} on {show_date}!"
    try:
        message = client.messages.create(body=body, from_=TWILIO_FROM, to=TWILIO_TO)
        logger.info(f"SMS sent: {message.sid}")
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}")

# SAFE QUIT
def safe_quit(driver):
    with contextlib.suppress(Exception):
        driver.quit()

# CHECK FUNCTION
def check_tickets():
    options = uc.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = None
    try:
        driver = uc.Chrome(options=options)
        wait = WebDriverWait(driver, 15)

        for theatre in THEATRES:
            key = f"{TARGET_DATE}:{MOVIE_NAME}:{theatre['code']}"
            if key in alerts_sent:
                logger.info(f"Already alerted for {key}, skipping.")
                continue

            url = (
                f"https://in.bookmyshow.com/cinemas/{theatre['city']}/{theatre['slug']}"
                f"/buytickets/{theatre['code']}/{TARGET_DATE}"
            )
            logger.info(f"Visiting: {url}")

            success = False
            for attempt in range(3):  # retry up to 3 times
                try:
                    driver.get(url)
                    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

                    # Look for movie links containing movie name (case-insensitive)
                    xpath = f"//a[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{MOVIE_NAME.lower()}')]"
                    movie_elements = driver.find_elements(By.XPATH, xpath)

                    if movie_elements:
                        logger.info(f"Found '{MOVIE_NAME}' at {theatre['slug']}")
                        send_sms(MOVIE_NAME, theatre['slug'], TARGET_DATE)
                        alerts_sent.add(key)
                        save_alerts()
                        success = True
                        break
                    else:
                        logger.info(f"Movie '{MOVIE_NAME}' not found at {theatre['slug']} on {TARGET_DATE}")
                        break  # no need to retry if page loaded fine

                except Exception as e:
                    logger.warning(f"Attempt {attempt+1} failed for {url}: {e}")
                    time.sleep(5)

            if not success:
                logger.info(f"No tickets found for {theatre['slug']} after retries.")

    except Exception as e:
        logger.error(f"Driver initialization or unexpected error: {e}")
        return 1

    finally:
        if driver:
            safe_quit(driver)  # prevents WinError 6
            logger.info("Browser closed gracefully.")

    return 0


if __name__ == "__main__":
    sys.exit(check_tickets())
