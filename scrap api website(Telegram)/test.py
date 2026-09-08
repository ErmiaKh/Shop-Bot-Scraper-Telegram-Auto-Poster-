from scraper import get_products

data = get_products()

print("TOTAL:", len(data))

for p in data:
    print(p)