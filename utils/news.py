import requests

def fetch_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey=your_news_api_key"
    response = requests.get(url)
    news_data = response.json()
    
    results = []
    for article in news_data['articles']:
        title = article['title']
        description = article['description']
        url = article['url']
        results.append({'title': title, 'description': description, 'url': url})
    
    return results
