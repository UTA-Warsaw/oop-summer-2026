import requests,random

website = requests.get('https://www.trthaber.com/haber/gundem/')

new = website.text.split('<a')   # metni linklere göre böl
choosen = random.choice(new)
print(choosen)