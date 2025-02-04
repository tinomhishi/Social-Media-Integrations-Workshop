import facebook

import json


with open('credentials.json') as f:
    data = json.load(f)
    PAGE_ID = data['FACEBOOK_PAGE_ID']
    ACCESS_TOKEN = data['FACEBOOK_PAGE_ACCESS_TOKEN']
    

def get_impressions():
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    insights = graph.get_object(f"{PAGE_ID}/insights/page_impressions")
    print(f'INSIGHTS: {insights}')
    
    
get_impressions()