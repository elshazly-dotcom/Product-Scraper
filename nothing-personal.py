import requests
from bs4 import BeautifulSoup

url = "https://www.nothing-personal.com/collections/tops"

response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

productList = soup.find_all('li', class_ = 'product-grid__item')

name = productList[0].find('h3').text

print(name)

price = productList[0].find('span', class_ = 'price').text.strip()

print(price)

productGallery = productList[0].find_all('div', class_ = 'product-media')

for div in productGallery:
    imgUrl = div.find('img')['src']
    print('https:' + imgUrl)