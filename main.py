
import requests
import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Đoạn này giúp Render thấy cổng mở và không báo lỗi nữa
def run_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), BaseHTTPRequestHandler)
    server.serve_forever()
threading.Thread(target=run_server, daemon=True).start()

def send_telegram_message(message):
    token = "7649557476:AAH66AAnP-pXl0_SsqTAn0uP896z6N5_x8E"
    chat_id = "7808566419"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Loi: {e}")

send_telegram_message("Bao cao chu nhan Atu: Bot da san sang!")

while True:
    print("Bot dang hoat dong...")
    time.sleep(60)
