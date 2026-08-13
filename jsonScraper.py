import requests
import json
from fake_useragent import UserAgent
import time
import random

# 1. Get user input and set up a randomized browser header
url = input("Enter URL: ")
name = input("Name of file: ")

ua = UserAgent()
headers = {"User-Agent": ua.random}

def isAvailable(data):
    if data["products"]:
        return True
    elif not data["products"]:
        return False

def fetchAllPage(baseUrl, headers):
    allProducts = []
    page = 1
    flag = True
    code = None

    # 2. Loop through all API pages until no products are left
    while True:
        url = f"{baseUrl}?page={page}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            code = response.status_code
        except requests.exceptions.RequestException as e:
            print(f"NETWORK ERROR: {e} — PLEASE TRY AGAIN AFTER A FEW MINUTES")
            flag = False
            break

        if code == 200:
            data = response.json()
        else:
            print(f"ERROR {code} PLEASE TRY AGAIN AFTER A FEW MINUTES")
            flag = False
            break

        if not isAvailable(data):
            break

        allProducts.extend(data["products"])
        page += 1
        
        # 3. Random delay to avoid hitting Shopify's rate limits
        time.sleep(random.randint(1, 3))

    print(f"COMPLETED: {flag}", f"STATUS: {code}", f"PAGES: {page - 1}")
    
    return {
        "meta": [{
            "isComplete": flag,
            "status": code,
            "pages": page - 1,
        }],
        "products": allProducts
    }

def main(url):
    # 4. Format the target URL to point to the correct JSON endpoint
    if url[-1] == '/':
        url = url[:-1]

    if "collections" in url:
        url += "/products.json"
    else:
        url += "/collections/all/products.json"

    data = fetchAllPage(url, headers)

    # 5. Save the raw product data and scrape metadata to JSON files
    with open(f"{name}RAW.json", "w") as f:
        products = data["products"]
        json.dump({"products": products}, f, indent=4)

    with open(f"{name}_meta.json", "w") as f:
        json.dump(data["meta"], f, indent=4)

main(url)