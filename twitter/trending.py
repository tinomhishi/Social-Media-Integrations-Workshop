import json

import tweepy


with open('credentials.json') as f:
    data = json.load(f)
    API_KEY = data['TWITTER_API_KEY']
    API_SECRET = data['TWIITER_API_SECRET']
    ACCESS_TOKEN = data['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = data['TWITTER_ACCESS_TOKEN_SECRET']
    BEARER_TOKEN = data['TWITTER_BEARER_TOKEN']


class TweetStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"New Tweet: {tweet.text}")


stream = TweetStream(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
stream.add_rules(tweepy.StreamRule("Trump"))
stream.filter()
