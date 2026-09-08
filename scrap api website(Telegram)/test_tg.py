import requests

TOKEN = "8570213899:AAE6_3mCDPq0F8W5oUy_3bkRpMAs0-xhwA8"
url = f"https://api.telegram.org/bot{TOKEN}/getMe"

print(requests.get(url, timeout=10).text)