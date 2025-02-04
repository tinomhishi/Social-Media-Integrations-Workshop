import json

import tweepy


with open('credentials.json') as f:
    data = json.load(f)
    API_KEY = data['TWITTER_API_KEY']
    API_SECRET = data['TWIITER_API_SECRET']
    ACCESS_TOKEN = data['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = data['TWITTER_ACCESS_TOKEN_SECRET']
    
    
def post_to_feed_api(tweet, img_url=None):
    print("Posting to Twitter Feed")
    print(f"API Key: {API_KEY[:5]}")
    print(f"API Secret: {API_SECRET[:5]}")
    print(f"Access Token: {ACCESS_TOKEN[:5]}")
    print(f"Access Token Secret: {ACCESS_TOKEN_SECRET[:5]}")
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    if img_url:
        api.update_status_with_media(tweet, img_url)
        
    print(f'Image: {img_url}')

    api.update_status(tweet)


post_to_feed_api("Clearly you've never made an omelette")