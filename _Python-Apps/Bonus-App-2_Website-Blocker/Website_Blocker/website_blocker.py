import time
from datetime import datetime as dt

hosts_temp = "hosts.txt"
# Windows filepath:
hosts_path = r"C:\Windows\System32\drivers\etc\hosts.txt"
# Mac/Linux filepath:
# hosts_path = "/etc/hosts"

# Variables for 'hosts' file modification
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com",
                "youtube.com", "www.youtube.com"]

# To run constantly in background
while True:
    year = dt.now().year
    month = dt.now().month
    today = dt.now().day
    if dt(year, month, today, 8) < dt.now() < dt(year, month, today, 16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("Fun hours...")
    time.sleep(5)