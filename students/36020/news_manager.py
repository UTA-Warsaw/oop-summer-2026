import requests 
import random
url = "https://newsdata.io/api/1/latest?apikey=pub_22fb861d4f494aad916681eb3d506f8e&q=bitcoin english"
raw_response = requests.get(url)
parsed_data = raw_response.json()
news_data = parsed_data["results"]
x = random.choice(news_data)
print(x["title"])
