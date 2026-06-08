import psutil
import schedule 
import time 
import asyncio
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

CPU_THRESHOLD = 80.0
RAM_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0

async def send_alert(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
def check_system():
    alerts = []

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        alerts.append(f"CPU usage is high: {cpu}%")
    if ram > RAM_THRESHOLD:
        alerts.append(f"RAM usage is high: {ram}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Disk usage is high: {disk}%")
    if alerts: 
        message = "⚠️ Server Monitor Alert!\n\n" + "\n".join(alerts)
        asyncio.run(send_alert(message))
    else:
        print("All systems are normal.")

schedule.every(60).seconds.do(check_system)
check_system()  # Initial check before starting the loop
while True:
    schedule.run_pending()
    time.sleep(1)