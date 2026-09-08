import requests

TOKEN = "8570213899:AAE6_3mCDPq0F8W5oUy_3bkRpMAs0-xhwA8"
CHAT_ID = "-1004359101673"

session = requests.Session()


def send_telegram(product):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    try:
        if not product.get("image"):
            print("⚠️ skip (no image):", product["title"])
            return

        caption = f"""
🛍 {product.get('title','محصول')}

🔗 لینک: {product.get('link','')}
"""

        img = session.get(product["image"], timeout=20)

        if img.status_code != 200:
            print("❌ image failed:", product["title"])
            return

        files = {
            "photo": ("img.jpg", img.content)
        }

        data = {
            "chat_id": CHAT_ID,
            "caption": caption
        }

        r = session.post(url, data=data, files=files, timeout=20)

        if r.status_code == 200:
            print("📤 sent:", product["title"])
        else:
            print("❌ Teleram error:", r.text)

    except Exception as e:
        print("❌ error sending:", e)