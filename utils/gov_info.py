import requests
from bs4 import BeautifulSoup

def fetch_gov_info(query):
    url = f"https://www.govinfo.gov/app/search/{query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.find_all('div', class_='result-item'):
        title = item.find('h3').text.strip()
        link = item.find('a')['href']
        summary = item.find('p', class_='summary').text.strip()
        results.append({'title': title, 'link': link, 'summary': summary})
    
    return results
