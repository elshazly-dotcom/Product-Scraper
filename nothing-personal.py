import requests
from bs4 import BeautifulSoup

url = "https://www.nothing-personal.com/collections/tops"

response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

productList = soup.find_all('li', class_ = 'product-grid__item')