import requests 
import random   
news_url = "https://news.kg/"

response = requests.get(news_url)

data = response.json()

news = data["hits"]

random_news = random.choice(news)

print("Random News")
print("Title:", random_news["title"])
print("Author:", random_news["author"])
print("URL:", random_news["url"])