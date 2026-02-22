
# --- THÔNG TIN CỦA ÔNG ATU ---

TOKEN = "8595834327:AAGjHFRpZBgc2AH9E_mrLdlQoJ5EC67sFjY"

CHAT_ID = "7808566419"



def send_telegram(message):

try:

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

params = {"chat_id": CHAT_ID, "text": message}

requests.get(url, params=params)

print("--- Da gui thong bao den dien thoai ---")

except Exception as e:

print(f"Loi gui tin nhan: {e}")



# Danh sach IP quen thuoc

known_ips = ["192.168.1.1", "192.168.1.48"]



print("========================================")

print(" BOT CANH CUA WIFI DANG KHOI DONG... ")

print("========================================")



send_telegram("Bao cao chu nhan Atu: Bot da san sang!")



while True:

print(f"[{time.strftime('%H:%M:%S')}] Dang quet mang...")

output = os.popen("sudo nmap -sn 192.168.1.0/24").read()

lines = output.splitlines()

for line in lines:

if "Nmap scan report for" in line:

ip = line.split()[-1].strip("()")

if ip not in known_ips:

canh_bao = f"CANH BAO: Thiet bi la ({ip}) vao Wifi!"

print(canh_bao)

send_telegram(canh_bao)

known_ips.append(ip)

time.sleep(60)
