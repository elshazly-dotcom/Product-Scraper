import requests
import json
from fake_useragent import UserAgent
import time
import random

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

    while True:
        url  = f"{baseUrl}?page={page}"
        response = requests.get(url, headers= headers)

        if response.status_code == 200:
            data = response.json()
        else:
            print(f"ERROR {response.status_code} PLEASE TRY AGAIN AFTER A FEW MINUTES")
            flag = False
            break
        
        if not isAvailable(data):
            break

        allProducts.extend(data["products"])
        page += 1
        time.sleep(random.randint(1,3))

    return {
        "isComplete": flag,
        "status": response.status_code,
        "pages": page - 1,
        "products": allProducts
    }

def main(url):
    if url[-1] == '/':
        url = url[:-1]

    if "collections" in url:
        url += "/products.json"
    else:
        url += "/collections/all/products.json"

    with open(f"{name}RAW.json", "w") as f:
        products = fetchAllPage(url, headers)
        json.dump(products, f, indent=4)

main(url)