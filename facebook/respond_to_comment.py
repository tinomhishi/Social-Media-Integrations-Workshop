import json

import requests


with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']

def respond_to_comment(comment_id, msg):
    url = f'https://graph.facebook.com/v22.0/{comment_id}/comments'
    params = {
        'access_token': ACCESS_TOKEN,
        'message': msg
    }
    r = requests.post(url, params=params)
    print(r.json())
    

respond_to_comment('122098223222762351_604706585765283', 'We will be seeing you really soon.')
    