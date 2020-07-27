import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver

# url = 'https://railway-platform.herokuapp.com/users'
# headers = {'Accept': 'application/json'}
# msg = requests.get(url, headers=headers).json().get('li')
# print(msg)

url = 'https://railway-platform.herokuapp.com/dashboard'
try:
    session = HTMLSession()
    response = session.get(url)

except requests.exceptions.RequestException as e:
    print(e)


soup = BeautifulSoup(requests.get(url).text, "html.parser")

for ele in soup.find("#root > div > div > div > div.mainDiv > div.row.dashboard_surveyDiv__1id8m > div.col-sm-5.dashboard_surveyRight__2uUNQ > div.dashboard_reponses__3KJ0u > ul > li:nth-child(2)"):
    print(ele)
