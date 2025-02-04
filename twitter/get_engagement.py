import json

import tweepy


with open('credentials.json') as f:
    data = json.load(f)
    API_KEY = data['TWITTER_API_KEY']
    API_SECRET = data['TWIITER_API_SECRET']
    ACCESS_TOKEN = data['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = data['TWITTER_ACCESS_TOKEN_SECRET']
    BEARER_TOKEN = data['TWITTER_BEARER_TOKEN']
    

def fetch_engagements(tweet_id):
    print(f"Fetching Engagements: {tweet_id}")
    print(f"API Key: {API_KEY[:5]}")
    print(f"API Secret: {API_SECRET[:5]}")
    print(f"Access Token: {ACCESS_TOKEN[:5]}")
    print(f"Access Token Secret: {ACCESS_TOKEN_SECRET[:5]}")
    print("Posting to Twitter Feed")
    
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    for like in tweepy.Cursor(api.get_favorites, id=tweet_id).items():
        print(like.user.screen_name)
    
    
fetch_engagements('1886390914412605589')