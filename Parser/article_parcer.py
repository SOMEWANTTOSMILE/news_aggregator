from Parser.news_parser import news_link
import requests
from bs4 import BeautifulSoup

for article_link in news_link:
    url = f'{article_link}'
# url = 'https://habr.com/ru/news/836798/'
    response = requests.get(url).text

    data = BeautifulSoup(response, 'html.parser')

    for article in data.find('div',
                             class_='article-formatted-body article-formatted-body article-formatted-body_version-2'):
        text = article
        print(f'art - {(text.prettify())}')
