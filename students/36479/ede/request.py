import requests
from bs4 import BeautifulSoup
import random

# Egyptian news website
url = "https://www.kingfut.com/"

# Send request
response = requests.get(url)

# Check if request worked
if response.status_code == 200:
    print("Connected successfully!\n")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines
    headlines = soup.find_all("a")

    news_list = []

    for headline in headlines:
        text = headline.get_text(strip=True)

        if text != "":
            news_list.append(text)

    # Print random news
    if len(news_list) > 0:
        random_news = random.choice(news_list)

        print("Random News:")
        print(random_news)
    else:
        print("No news found.")

else:
    print("Failed to connect.")