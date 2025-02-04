import json

import requests

with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']
    

def delete_post(post_id):
    url = f"https://graph.facebook.com/v22.0/{post_id}?access_token={ACCESS_TOKEN}"
    r = requests.delete(url)
    print(r.json())
    
delete_post('587706781084458_122098225376762351')