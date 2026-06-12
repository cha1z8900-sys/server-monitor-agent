# Server Monitor Agent

Automation agent that monitors server metrics (CPU, RAM, Disk) and sends Telegram alerts when thresholds are exceeded.

## What it does
- Monitors CPU, RAM, and disk usage every 60 seconds
- Sends instant Telegram alert when any metric exceeds threshold
- Runs continuously in the background

## Tech stack
- Python
- psutil
- python-telegram-bot
- schedule

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install psutil python-telegram-bot schedule python-dotenv`
5. Create `.env` file with your credentials:TELEGRAM_TOKEN=your_token_here
CHAT_ID=your_chat_id_here
6. Run: `python monitor.py`

## Configuration
Edit thresholds in `monitor.py`:
- `CPU_THRESHOLD` — default 80%
- `RAM_THRESHOLD` — default 80%
- `DISK_THRESHOLD` — default 90%