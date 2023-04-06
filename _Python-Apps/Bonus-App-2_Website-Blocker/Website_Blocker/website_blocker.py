import time
from datetime import datetime as dt

# Windows filepath:
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# Mac/Linux filepath:
# hosts_path = "/etc/hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com",
                "youtube.com", "www.youtube.com"]

while True:
    year = dt.now().year
    month = dt.now().month
    today = dt.now().day
    if dt(year, month, today, 8) < dt.now() < dt(year, month, today, 16):
        print("Working hours...")
    else:
        print("Fun hours...")
    time.sleep(5)