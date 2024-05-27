
```

██ ▄█▀▓█████▓██   ██▓  ██████ 
██▄█▒ ▓█   ▀ ▒██  ██▒▒██    ▒  
▓███▄░ ▒███    ▒██ ██░░ ▓██▄   
▓██ █▄ ▒▓█  ▄  ░ ▐██▓░  ▒   ██▒
▒██▒ █▄░▒████▒ ░ ██▒▓░▒██████▒▒
▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░
░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ░ ░▒  ░ ░
░ ░░ ░    ░   ▒ ▒ ░░  ░  ░  ░  
░  ░      ░  ░░ ░           ░  
              ░ ░ 
```
(am all for constructive criticism - if you are a skilled/proficient prgrammer or engineer of any sorts and you think my tool sucks let me know why and if it is applicable will burn it with fire and try again until I eventually come back with the GREATEST OSINT TOOL TO EVER EXIST! If you have any problems, or need any help feel free to start a discussion I would love to connect - s or make a pull request! But I really hope you all do enjoy and if there's something you'd like to see that isn't directly SCRIPT/TOOL related incorporated please feel free to ask)


# InsightGatherer

## InsightGatherer is an OSINT (Open Source Intelligence) tool that aggregates information from various public sources, including government databases, social media, news articles, geolocation data, domain and IP information, and visualizations.

### Features

- **Government Information**: Fetches public government records and documents.
- **Social Media**: Retrieves recent tweets related to a search query.
- **News**: Gathers news articles matching the search query.
- **Geospatial Data**: Provides geolocation information based on the search query.
- **Domain Information**: Fetches domain registration and DNS information.
- **Visualization**: Generates visual representations of the collected data.

## Setup

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Installation

1. **Clone the repository:**

```
     bash
   git clone https://github.com/yourusername/InsightGatherer.git
   cd InsightGatherer
```

# Create and activate a virtual environment:

``` python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
# Install dependencies:

```pip install -r requirements.txt```

# Set up environment variables:

``Create a .env file in the root directory and add your API keys:``

```
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
NEWS_API_KEY=your_news_api_key
```
# Run the application:

```python app.py```

Access the application at http://127.0.0.1:5000.

# Deployment

- Deploying to Heroku
------Log in to Heroku:
```heroku login```

# Create a Heroku app
```heroku create insightgatherer```

# Add a Procfile to your project root:
```
web: python app.py
```
# Add a `requiremenmts.txt` file

```
Flask
requests
beautifulsoup4
tweepy
geopy
whois
dnspython
matplotlib
gunicorn
```
# Add a `runtime.txt` file

```python-3.8.10```

# Commit in changes: 

```git add Procfile requirements.txt runtime.txt git commit -m "Add Heroku deployment files"```

# Push to Heroku:

```git push heroku master```

# Scale your application

```heroku ps:scale web=1```

# Open your application 

```heroku open```

# Setting you Environment Variable on Heroku

## Set your Environment Variables:

```
heroku config:set TWITTER_API_KEY=your_twitter_api_key
heroku config:set TWITTER_API_SECRET=your_twitter_api_secret
heroku config:set NEWS_API_KEY=your_news_api_key
```

# Director STRUCTURE:

```
osint_tool/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── visualization.png
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
├── Procfile
├── runtime.txt
└── README.md
```

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.


