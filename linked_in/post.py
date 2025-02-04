import requests
import json

with open('credentials.json') as f:
    data = json.load(f)
    ACCESS_TOKEN = data['LINKEDIN_ACCESS_TOKEN']

access_token = ACCESS_TOKEN

# The endpoint to get your profile data
url = 'https://api.linkedin.com/v2/me'

# Set the headers for authorization
headers = {
    'Authorization': f'Bearer {access_token}',
    'X-Restli-Protocol-Version': '2.0.0',
}

# Make the GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Get your LinkedIn URN from the response
    user_urn = data['id']
    print(f"Your LinkedIn URN: urn:li:person:{user_urn}")
else:
    print(f"Error: {response.status_code} - {response.text}")



# import json

# import requests


# with open('credentials.json') as f:
#     data = json.load(f)
#     ACCESS_TOKEN = data['LINKEDIN_ACCESS_TOKEN']
    
    
# def post_to_feed(msg, img_url=None):
#     url = 'https://api.linkedin.com/v2/ugcPosts'

#     headers = {
#         'Authorization': f'Bearer {ACCESS_TOKEN}',
#         'X-Restli-Protocol-Version': '2.0.0',
#         'Content-Type': 'application/json',
#     }

#     post_data = {
#         "author": f"urn:li:person:Tinotenda Mhishi",
#         "lifecycleState": "PUBLISHED",
#         "specificContent": {
#             "com.linkedin.ugc.ShareContent": {
#                 "shareCommentary": {
#                     "text": "This is a sample post text!"
#                 },
#                 "shareMediaCategory": "NONE"
#             }
#         },
#         "visibility": {
#             "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
#         }
#     }

#     response = requests.post(url, headers=headers, json=post_data)

#     print(response.json())
    

# post_to_feed('Clearly')