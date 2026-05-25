import requests
import random

url = "https://www.hurriyet.com.tr/"
response = requests.get(url)

titles = response.text.split('"title":"')

news = []

for t in titles[1:]:
    title = t.split('"')[0]
    if len(title) > 10:  # çok kısa çöp verileri filtreler
        news.append(title)

print("Random news:")
print(random.choice(news))