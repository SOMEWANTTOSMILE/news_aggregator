import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/news/'
response = requests.get(url).text
news_link = []

data = BeautifulSoup(response, 'html.parser')

for article in data.find_all('h2', class_='tm-title tm-title_h2'):
    title = article.a.span.text
    link = 'https://habr.com'+article.a['href']
    news_link.append(link)

print(news_link)