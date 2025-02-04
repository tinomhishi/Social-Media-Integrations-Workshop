import json

import requests

with open('credentials.json') as f:
    data = json.load(f)
    CLIENT_ID = data['LINKEDIN_CLIENT_ID']
    CLIENT_SECRET = data['LINKEDIN_CLIENT_SECRET']

TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

payload = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

response = requests.post(TOKEN_URL, data=payload)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code}, {response.text}")