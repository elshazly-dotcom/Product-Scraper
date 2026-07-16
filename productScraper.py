import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nothing-personal.com/collections/all/products.json"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

response = requests.get(url, headers= headers)

if response.status_code == 200:
    data = response.json()

    with open ("website.json", "w") as f:
        json.dump(data, f, indent=4)