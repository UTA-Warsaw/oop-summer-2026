import requests
from bs4 import BeautifulSoup
import random

def get_random_news_with_content():
    base_url = "https://www.hurriyet.com.tr"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = soup.select('a[href*="/gundem/"], a[href*="/dunya/"], a[href*="/ekonomi/"]')
        
        valid_news = []
        for link in links:
            title = link.get_text(strip=True)
            href = link.get('href')
            if len(title) > 30 and href.startswith('/'):
                valid_news.append((title, base_url + href))

        if valid_news:
            selected_title, selected_url = random.choice(valid_news)
            
            detail_response = requests.get(selected_url, headers=headers)
            detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
            
            paragraphs = detail_soup.find_all('p')
            content = "\n".join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 40])

            print(f"HEADLINE: {selected_title}")
            print("-" * 50)
            print(f"CONTENT:\n{content[:1000]}...") 
        else:
            print("No news links found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_random_news_with_content()