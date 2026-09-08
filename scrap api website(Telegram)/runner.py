import time
from main import run_job

while True:
    print("\n🚀 Running job...")

    try:
        run_job()
    except Exception as e:
        print("❌ Error:", e)
        time.sleep(1200)
        continue