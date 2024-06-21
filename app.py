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
    app.run(debug=False) # Place to True to ENABLE DEBUG MODE  (WARNING SECURITY RISK FOR UNTRUSTED USERS)
