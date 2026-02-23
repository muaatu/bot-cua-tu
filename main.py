import requests
import time

def send_telegram_message(message):
    token = "7649557476:AAH66AAnP-pXl0_SsqTAn0uP896z6N5_x8E"
    chat_id = "7052737604"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Loi: {e}")

# Thong bao khi bot bat dau chay
send_telegram_message("Bao cao chu nhan Atu: Bot da san sang!")

while True:
    print("Bot dang hoat dong...")
    time.sleep(60)
