from scraper import get_products
from telegram import send_telegram
from storage import load_sent, save_sent, is_sent


def run_job():
    products = get_products()
    sent = load_sent()

    print("TOTAL:", len(products))

    for p in products:

        if is_sent(p["link"], sent):
            print("⏭ skipped:", p["title"])
            continue

        try:
            send_telegram(p)

            sent.add(p["link"])
            save_sent(sent)

            print("✔ sent:", p["title"])

        except Exception as e:
            print("❌ error:", e)