
# Social Media API Integration Using Python

## Facebook:
   - The largest social media platform, with over 2.9 billion monthly active users. Hugest market for an audience.
   - Includes personal profiles, business pages, groups, and advertising tools.
1. Features:
   - Facebook Pages: Spaces for businesses to engage with customers.
   - Facebook Ads: Targeted campaigns and analytics.
   - Facebook Groups: Community building tools.
   - Facebook Live: Livestreaming for engagement.
2. Business Opportunities:
   - Content Creation Management.
   - Engagement Metrics.
   - Ad Campaign Management and Analytics
3. SDK:
  - Installation
   `pip install facebook-sdk`
  - Posting To Page
    ```
    import facebook
    
    # Initialize the Graph API with an access token
    access_token = 'YOUR_ACCESS_TOKEN'
    graph = facebook.GraphAPI(access_token)
    
    # Post to a page
    graph.put_object("PAGE_ID", "feed", message="Hello, Facebook!")
    ```
  - Getting Insights
    ```
    # Retrieve page insights
    insights = graph.get_object("PAGE_ID/insights/page_impressions")
    print(insights)
    ```
4. Case Study:
   - A local donut shop wants to advertise various donut recipes. Can create posts about daily specials and retrieve engagement metrics and refine approach.
   - Example Mambo's Content. Topical, humorous massive engagement. Question is what do you remember more, the joke or the product they are promoting.
   
## Twitter
  - Micro blogging site.
  - 330 million active users.
  - Real-Time updates for events
  - Hashtag Driven Threads

1. Features:
   - Tweets: 280-character text posts. Can include pictures and video
   - Hashtags: Grouping content
   - Trending Topics: Regional based topics with high level of engagement
   - Twitter Adds: Promote Tweets and accounts
2. Business Opportunities:
   - Posting tweets and reposting.
   - Monitoring Tweets, Mentions, Hashtags.
   - Analysing tweet peformance. Metrics like reposts/retweets, comments.
3. SDK:
   - Installation
   `pip install tweepy`
   - Posting\Tweeting
   ```
   # Authenticate
    auth = tweepy.OAuth1UserHandler("CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
    api = tweepy.API(auth)
    
    # Post a tweet
    api.update_status("Hello, Twitter!")
   ```
   - Monitoring Engagement
     ```
     # Retrieve mentions
      mentions = api.mentions_timeline()
      for mention in mentions:
          print(mention.text)
     ```
  4. Case Study
     - Vacancy Mail. Posting vacancies periodically on official twitter account.

## Tik Tok
- Short-form video platform with over 1 billion monthly active users.
- Largely Gen Z and under 30
- Algorithm that promotes engagement and maximizes attention grabbing.
- Viral content and creation tools

1. Features
 - Videos
 - Tik Tok Ads
 - Creator market place to engage with other creators.
 - Live streaming
2. Business Opportunities
 - Content Creation and Management
 - Post Creation Metrics
 - Ad Campaign Management
3. SDK
   - Installation
     `pip install TikTokApi`
   - Posting Video
     ```
     from TikTokApi import TikTokApi

      # Authenticate
      api = TikTokApi()
      
      # Post a video
      api.upload_video("path/to/video.mp4", description="Hello, TikTok!")
     ```
   - Getting Video Metrics
     ```
     # Retrieve video metrics
      metrics = api.get_video_metrics("VIDEO_ID")
      print(metrics)
     ```
4. Case Study
   - George wants to share how to share recipes for his food truck. Adhering to the carnivore diet principles. Witty funnys post informative and engaging.
     
