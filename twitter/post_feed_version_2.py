import json

import tweepy


with open('credentials.json') as f:
    data = json.load(f)
    API_KEY = data['TWITTER_API_KEY']
    API_SECRET = data['TWIITER_API_SECRET']
    ACCESS_TOKEN = data['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = data['TWITTER_ACCESS_TOKEN_SECRET']
    BEARER_TOKEN = data['TWITTER_BEARER_TOKEN']
    

def post_to_feed_api(tweet_text, img_url=None):
    print("Posting to Twitter Feed")
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
    
    
    if img_url:
        client.media_upload(img_url)

    response = client.create_tweet(text=tweet_text)
    print(response)
    
post_to_feed_api("Clearly you've never made an omelette")