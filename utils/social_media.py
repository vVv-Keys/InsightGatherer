import tweepy

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
