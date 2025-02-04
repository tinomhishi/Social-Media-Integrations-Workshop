import json

import requests


with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']


def get_page_engagements():
    url = f'https://graph.facebook.com/v22.0/{PAGE_ID}/insights'
    params = {
        'metric': 'page_post_engagements',
        'access_token': ACCESS_TOKEN
    }
    r = requests.get(url, params=params)
    data = r.json()
    print(data)
    
def get_post_engagements(post_id):
    url = f'https://graph.facebook.com/v22.0/{post_id}/comments'
    params = {
        'access_token': ACCESS_TOKEN,
        'fields': 'id,message,created_time,from',
        'limit': 100
    }

    r = requests.get(url, params=params)
    data = r.json()
    print(data)


# get_post_engagements('587706781084458_122098786346762351')
get_page_engagements()