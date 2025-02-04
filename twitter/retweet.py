import json

import tweepy


with open('credentials.json') as f:
    data = json.load(f)
    API_KEY = data['TWITTER_API_KEY']
    API_SECRET = data['TWIITER_API_SECRET']
    ACCESS_TOKEN = data['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = data['TWITTER_ACCESS_TOKEN_SECRET']
    BEARER_TOKEN = data['TWITTER_BEARER_TOKEN']
    

def retweet(tweet_id):
    print(f"Retweeting: {tweet_id}")
    print(f"API Key: {API_KEY[:5]}")
    print(f"API Secret: {API_SECRET[:5]}")
    print(f"Access Token: {ACCESS_TOKEN[:5]}")
    print(f"Access Token Secret: {ACCESS_TOKEN_SECRET[:5]}")
    print("Posting to Twitter Feed")
    
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    client.unretweet(tweet_id)
    
retweet('1851463451929186504')