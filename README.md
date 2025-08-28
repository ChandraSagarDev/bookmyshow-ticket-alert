# 🎬 BookMyShow Movie Ticket Availability Checker

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

A Python script that automatically checks for movie ticket availability on BookMyShow and notifies you via SMS when tickets become available for your preferred movie, date, and theaters.

## 🚀 Features

- **Real-time Monitoring**: Continuously checks for ticket availability
- **Theater-Specific Alerts**: Get notified for specific theaters of your choice
- **Smart Notifications**: Instant SMS alerts via Twilio when tickets become available
- **Duplicate Prevention**: Avoids spamming with state tracking
- **Multi-Theater Support**: Monitor multiple theaters simultaneously
- **Easy Configuration**: Simple JSON-based setup

## 📋 Prerequisites

- Python 3.7 or higher
- Twilio Account (for SMS notifications)
- BookMyShow account (for reference)

## 🔐 Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_FROM=+1234567890  # Your Twilio phone number
TWILIO_TO=+1234567890    # Your personal phone number
```

Never commit the `.env` file to version control!

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/myShowNotify.git
   cd myShowNotify
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application**
   - Copy `config.example.json` to `config.json`
   - Update the configuration with your preferences (see Configuration section below)
   - Add your Twilio credentials

## ⚙️ Configuration

Edit the `config.json` file with your preferences:

```json
{
    "movie_name": "Movie Name",
    "theatres": [
        {
            "name": "Theatre Name",
            "code": "theatre-code"
        }
    ],
    "date": "YYYYMMDD",
    "twilio": {
        "account_sid": "your_account_sid",
        "auth_token": "your_auth_token",
        "from_number": "+1234567890",
        "to_number": "+1234567890"
    },
    "check_interval": 300,
    "debug": false
}
```

## 🚦 Usage

1. Update the `config.json` with your preferences
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will run continuously, checking for ticket availability at the specified interval

## 📞 Support

For issues and feature requests, please [open an issue](https://github.com/yourusername/myShowNotify/issues).

## 🙏 Acknowledgments

- BookMyShow for their ticketing platform
- Twilio for SMS notifications
- Python community for awesome libraries

---

<div align="center">
  Made with ❤️ by Sagar | 🤖 Automated with Python
</div>
