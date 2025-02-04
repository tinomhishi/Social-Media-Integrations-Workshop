import json

import requests

with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']


def get_page_posts():
    url = f"https://graph.facebook.com/v22.0/{PAGE_ID}/posts?access_token={ACCESS_TOKEN}"
    r = requests.get(url)
    data = r.json().get('data')
    post_ids = [{i.get('id'): i.get('message')} for i in data]
    print(post_ids)
    return


get_page_posts()