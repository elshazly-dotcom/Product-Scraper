import requests
import json

url = input("Enter URL: ")

if "collections" in url:
    url += "/products.json"
else:
    url += "/collections/all/products.json"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

response = requests.get(url, headers= headers)

if response.status_code == 200:
    data = response.json()

    with open ("website.json", "w") as f:
        json.dump(data, f, indent=4)