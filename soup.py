import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://railway-platform.herokuapp.com/dashboard'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

price = soup.find_all("div")
# attrs={"class": "dashboard_reponses__3KJ0u"})
print(price)
