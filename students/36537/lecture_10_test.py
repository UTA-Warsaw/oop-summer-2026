import requests
import random
from bs4 import BeautifulSoup

news = requests.get('https://www.pravda.com.ua/news/')


soup = BeautifulSoup(news.text, 'html.parser')

# Find all divs with the class 'article_title'
title_divs = soup.find_all('div', class_='article_title')

# Extract text, stripping away the extra whitespace/newlines
news_titles = [div.get_text(strip=True) for div in title_divs]

one = random.choice(news_titles)
print(one)