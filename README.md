# 🎬 BookMyShow Ticket Alert Bot

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

Get instant **SMS notifications** when movie tickets go live on  
[BookMyShow](https://bookmyshow.com)!  
This bot automatically monitors your selected **movie, date, and
theatres** and sends you an alert via **Twilio SMS** as soon as bookings
open.

---

## 🚀 Features

- **Real-time Monitoring**: Continuously checks for ticket availability  
- **Theater-Specific Alerts**: Get notified for specific theaters of your choice  
- **Smart Notifications**: Instant SMS alerts via Twilio when tickets become available  
- **Duplicate Prevention**: Avoids spamming with state tracking (`alerts_sent.json`)  
- **Multi-Theater Support**: Monitor multiple theaters simultaneously  
- **Easy Configuration**: Simple JSON-based setup  
- **Headless Mode** (no Chrome window) for silent background execution  

---

## 📋 Prerequisites

- Python **3.7+**  
- [Twilio Account](https://www.twilio.com/) (for SMS notifications)  
  👉 [Twilio Setup Guide](https://www.twilio.com/docs/sms/quickstart/python)  
- BookMyShow account (for reference)  

---

## 📂 Project Structure

```
📦 bookmyshow-ticket-alert
 ┣ 📜 check_tickets.py       # main script
 ┣ 📜 config.json            # configuration file
 ┣ 📜 config.example.json    # example config template
 ┣ 📜 alerts_sent.json       # state storage (auto-created)
 ┣ 📜 requirements.txt       # dependencies
 ┗ 📜 README.md              # documentation
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_FROM=+1234567890  # Your Twilio phone number
TWILIO_TO=+1234567890    # Your personal phone number
```

---

## 🛠 Installation

1️⃣ **Clone Repo**

```bash
git clone https://github.com/your-username/bookmyshow-ticket-alert.git
cd bookmyshow-ticket-alert
```

2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Configure the Application**
- Copy `config.example.json` → `config.json`  
- Update with your preferences (see **Configuration** below)  
- Add your Twilio credentials  

---

## ⚙️ Configuration

Edit the `config.json` file with your preferences:

```json
{
  "movie_name": "Coolie",
  "date": "20250814",
  "theatres": [
    {
      "city": "ernakulam",
      "slug": "pvr-lulu-kochi",
      "code": "PVLC"
    },
    {
      "city": "ernakulam",
      "slug": "vanitha-cineplex-rgb-laser-4k-3d-atmos-edappally",
      "code": "VMHE"
    }
  ],
  "headless": true,
  "check_interval": 300,
  "debug": false
}
```

### 🔑 Config Parameters:
- `movie_name`: Name of the movie to monitor  
- `date`: Date in `YYYYMMDD` format  
- `theatres`: List of theatres (`city`, `slug`, `code`)  
- `headless`: Run Chrome silently without window  
- `check_interval`: Interval in seconds for continuous checking  
- `debug`: Enable verbose logging  

### 🎟️ How to find `slug`, `city`, and `code`  
1. Go to [BookMyShow Cinemas](https://in.bookmyshow.com/cinemas)  
2. Select your city and open your theatre’s page  
   - Example URL:  
     ```
     https://in.bookmyshow.com/cinemas/ernakulam/pvr-lulu-kochi/PVLC
     ```
   - Here:  
     - `city` → `ernakulam`  
     - `slug` → `pvr-lulu-kochi`  
     - `code` → `PVLC`  

---

## ▶️ Usage

Run once:

```bash
python check_tickets.py
```

Run continuously every 5 minutes (built-in loop):

```bash
python check_tickets.py --loop 5
```

Or schedule with:  
- **Windows Task Scheduler** → run every X minutes  
- **Linux/macOS cron** → `*/5 * * * * python /path/to/check_tickets.py`  

---

## 📱 Example SMS Alert

```
🎉 Tickets for 'Coolie' are LIVE at pvr-lulu-kochi on 2025-08-14!
```

---

## 🛠️ Tech Stack

- [Python 3](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/) + [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)  
- [Twilio SMS API](https://www.twilio.com/sms)  
- [dotenv](https://pypi.org/project/python-dotenv/)  

---

## 📞 Support

For issues and feature requests, please [open an issue](https://github.com/your-username/bookmyshow-ticket-alert/issues).

---

## 🙏 Acknowledgments

- [BookMyShow](https://bookmyshow.com) for their ticketing platform  
- [Twilio](https://www.twilio.com/) for SMS notifications  
- Python community for awesome libraries  

---

<div align="center">

Made with ❤️ by Sagar | 🤖 Automated with Python  

</div>  
