import json
import os

SENT_FILE = "sent.json"


def load_sent():
    if not os.path.exists(SENT_FILE):
        return set()

    try:
        with open(SENT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data if isinstance(data, list) else [])
    except:
        return set()


def save_sent(sent_set):
    tmp_file = SENT_FILE + ".tmp"

    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(list(sent_set), f, ensure_ascii=False, indent=2)

    os.replace(tmp_file, SENT_FILE)


def is_sent(link, sent_set):
    return link in sent_set