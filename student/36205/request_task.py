import requests
import random

r = requests.get("https://www.sozcu.com.tr")

print(r.text)

news = [
    "Economy is changing",
    "Fenerbahce is winning",
    "Weather is sunny"
]

selected_news = random.choice(news)

print(selected_news)