import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver

url = 'https://railway-platform.herokuapp.com/dashboard'

try:
    session = HTMLSession()
    response = session.get(url)

except requests.exceptions.RequestException as e:
    print(e)


soup = BeautifulSoup(requests.get(url).text, "lxml")

for ele in soup.find_all("noscript"):
    print(ele.text)
# elements = response.html.find('h1', first=True)
# print(elements.text)
