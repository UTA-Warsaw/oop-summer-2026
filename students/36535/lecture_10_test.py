import requests
import random

url = "https://www.trthaber.com"

response = requests.get(url)

lines = response.text.splitlines()

titles = []

for line in lines:
    if 'title="' in line:
        titles.append(line)

random_title = random.choice(titles)

print("Random News:")
print(random_title)