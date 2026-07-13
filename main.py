import requests
from bs4 import BeautifulSoup

url = "https://www.nothing-personal.com/collections/tops"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
