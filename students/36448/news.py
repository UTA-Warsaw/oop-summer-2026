
#import requests
#x = requests.get('https://www.trthaber.com/')
#print(x.text)

import requests
from bs4 import BeautifulSoup
import random
url = 'https://www.trthaber.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
basliklar = soup.find_all(['h1', 'h2', 'h3', 'h4'])
temiz_basliklar = [b.get_text(strip=True) for b in basliklar if len(b.get_text(strip=True)) > 10]
if temiz_basliklar:
    rastgele_haber = random.choice(temiz_basliklar)
    print(rastgele_haber)


#import requests
#import random
#url = "https://www.trthaber.com/"
#response = requests.get(url)
#html = response.text
#titles = []
#for line in html.split("\n"):
#    if "<h3" in line:
#        clean + ine.strip()
#        titles.append(clean)
#if not titles:
#    print("Nope")
#else:
#    random_title = random.choice(titles)
#print("Random News")
#print(random_title)
