# PublicEYE-OSINT


This custom OSINT tool provides a comprehensive solution for gathering and analyzing various types of open-source information. It integrates multiple sources of data, such as government information, social media, news, geospatial data, and domain/IP information, while also offering visualization capabilities.


# Directory Structure

```
osint_tool/
├── app.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── index.html
│   └── results.html
├── utils/
│   ├── gov_info.py
│   ├── social_media.py
│   ├── news.py
│   ├── geospatial.py
│   ├── domain_ip.py
│   └── visualization.py
├── requirements.txt
└── README.md
```

# Simple CODE app.py - Main application

```
from flask import Flask, render_template, request
from utils.gov_info import fetch_gov_info
from utils.social_media import fetch_social_media
from utils.news import fetch_news
from utils.geospatial import fetch_geolocation
from utils.domain_ip import fetch_domain_info
from utils.visualization import create_visualization

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    gov_info = fetch_gov_info(query)
    social_media = fetch_social_media(query)
    news = fetch_news(query)
    geolocation = fetch_geolocation(query)
    domain_info = fetch_domain_info(query)
    visualization = create_visualization(query)

    return render_template('results.html', query=query, gov_info=gov_info,
                           social_media=social_media, news=news,
                           geolocation=geolocation, domain_info=domain_info,
                           visualization=visualization)

if __name__ == '__main__':
    app.run(debug=True)
```
# utils/gov_info.py - Fetching public government information

```
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

```
# utils/social_media.py - Fetching social media information

```
import tweepy
import json

def fetch_social_media(query):
    api_key = 'your_twitter_api_key'
    api_secret_key = 'your_twitter_api_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search(q=query, count=10)
    results = [{'user': tweet.user.screen_name, 'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
    
    return results
```
# utils/news.py - Fetching news information

```
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
```
# utils/geospatial.py - Fetching geospatial information

```
from geopy.geocoders import Nominatim

def fetch_geolocation(query):
    geolocator = Nominatim(user_agent="osint_tool")
    location = geolocator.geocode(query)
    return {'address': location.address, 'latitude': location.latitude, 'longitude': location.longitude}
```
# utils/domain_ip.py - Fetching domain and IP information

```
import whois
import dns.resolver

def fetch_domain_info(domain):
    domain_info = whois.whois(domain)
    dns_info = dns.resolver.resolve(domain, 'A')
    ip_addresses = [ip.to_text() for ip in dns_info]
    
    return {'domain_info': domain_info, 'ip_addresses': ip_addresses}
```
 
# utils/visualization.py - Creating visualizations

```
import matplotlib.pyplot as plt

def create_visualization(data):
    # Example: Creating a bar chart of some data
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    plt.savefig('static/images/visualization.png')
    return 'static/images/visualization.png'
```

# Web Interface (HTML) - templates/index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSINT Tool</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>OSINT Tool</h1>
        <form action="/search" method="POST">
            <input type="text" name="query" placeholder="Enter search query">
            <button type="submit">Search</button>
        </form>
    </div>
</body>
</html>
```
# templates/results.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results for {{ query }}</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Results for "{{ query }}"</h1>

        <h2>Government Information</h2>
        <ul>
            {% for item in gov_info %}
            <li><a href="{{ item.link }}">{{ item.title }}</a> - {{ item.summary }}</li>
            {% endfor %}
        </ul>

        <h2>Social Media</h2>
        <ul>
            {% for tweet in social_media %}
            <li>{{ tweet.user }}: {{ tweet.text }} ({{ tweet.created_at }})</li>
            {% endfor %}
        </ul>

        <h2>News</h2>
        <ul>
            {% for article in news %}
            <li><a href="{{ article.url }}">{{ article.title }}</a> - {{ article.description }}</li>
            {% endfor %}
        </ul>

        <h2>Geolocation</h2>
        <p>{{ geolocation.address }} ({{ geolocation.latitude }}, {{ geolocation.longitude }})</p>

        <h2>Domain Information</h2>
        <p>{{ domain_info.domain_info }}</p>
        <p>IP Addresses: {{ domain_info.ip_addresses }}</p>

        <h2>Visualization</h2>
        <img src="{{ visualization }}" alt="Visualization">
    </div>
</body>
</html>
```

# Dependencies - requirements.txt

```
Flask
requests
beautifulsoup4
tweepy
geopy
whois
dnspython
matplotlib
```

# Conclusion

``` 
Conclusion
This custom OSINT tool provides a comprehensive solution for gathering and analyzing various types of open-source information. It integrates multiple sources of data, such as government information, social media, news, geospatial data, and domain/IP information, while also offering visualization capabilities. This example can be further extended to include more specialized features and functionalities based on the specific needs of the investigation.```
