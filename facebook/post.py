import json

import facebook


# Get config from credentials.json

with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']


def post_to_facebook(message, image_url=None):
    print('Posting to Facebook')
    print('Message:', message)
    print('Image:', image_url or '-')
    print('Page ID:', PAGE_ID)
    print('Access Token:', ACCESS_TOKEN[:10])
    
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    if image_url:
        graph.put_photo(image=open(image_url, 'rb'), message=message)
    else:
        graph.put_object(PAGE_ID, "feed", message=message)
    print("Posted to Facebook")
    return True


# post_to_facebook("I think you're confusing peace with quiet.")
post_to_facebook(
    "I was meant to be beautiful. The world would have looked to the sky and seen hope...seen mercy.",
    image_url='img/img_1.jpg'
    
)