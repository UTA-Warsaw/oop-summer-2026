import requests
x = requests.get('https://www.w3schools.com/python/module_requests.asp')
print(x.text)