from playwright.sync_api import sync_playwright


def get_products():
    url = "https://hanamood.ir/"
    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        list_page = browser.new_page()
        list_page.goto(url, timeout=60000)
        list_page.wait_for_timeout(3000)

        items = list_page.query_selector_all("div.product-wrapper")

        print("TOTAL FOUND:", len(items))

        product_page = browser.new_page()

        for item in items:
            try:
                a_tag = item.query_selector("a")
                if not a_tag:
                    continue

                link = a_tag.get_attribute("href")
                if not link:
                    continue

                img_el = item.query_selector("img")
                image = img_el.get_attribute("src") if img_el else None

                # 🔥 IMPORTANT: use separate page
                product_page.goto(link, timeout=60000, wait_until="domcontentloaded")

                title_el = product_page.query_selector("h1")
                title = title_el.inner_text().strip() if title_el else "محصول"

                if not image:
                    img2 = product_page.query_selector(".woocommerce-product-gallery__image img")
                    image = img2.get_attribute("src") if img2 else None

                products.append({
                    "title": title,
                    "link": link,
                    "image": image
                })

                print("✔ scraped:", title)

            except Exception as e:
                print("error:", e)

        product_page.close()
        list_page.close()
        browser.close()

    return products