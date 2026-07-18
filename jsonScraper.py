import requests
import json
from fake_useragent import UserAgent

url = input("Enter URL: ")

name = input("Name of file: ")

if url[-1] == '/':
    url = url[:-1]

if "collections" in url:
    url += "/products.json"
else:
    url += "/collections/all/products.json"

ua = UserAgent()

headers = {"User-Agent": ua.random}

response = requests.get(url, headers= headers)

if response.status_code == 200:
    data = response.json()

    with open (f"{name}.json", "w") as f:
        json.dump(data, f, indent=4)
else:
    print(response.status_code)