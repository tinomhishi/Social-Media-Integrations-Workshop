# Social Media API Integrations

Social Media integrations facilitate the streamlining of operations that do with communications and engagement with customers and potential customers by.
1. Improving brand visibility and engagement with automated posting.
2. Provides concrete means to evaluate engagement efforts via impressions and engagement. Also presents the opportunity with sentiment analysis using libraries like spacy and Textblob. Demographic analysis.
3. Automated query responses using menu based chatbot responses to direct messages.
4. Lead generation and conversion.

## SDKs
### Facebook
https://github.com/mobolic/facebook-sdk
- Features include post management, fetching user data and impressions
- Third Party
### Twitter/X
https://www.tweepy.org/
-  Post, Repost, Follow, Unfollow, Track trends
- Third Party
- ### WhatsApp

## Using SDKs v Direct Calling
### SDKs
- Ease of use.
- Community supported SDKs like tweepy are well maintained and upto to date with the Twitter API.
- Faster feature integration.
- Black box due to abstraction.
- Limits development to what the SDK supports and prioritizes.
- Updates can break code.
- Some SDK are officially maintained by Platform Providers like facebook. For example https://github.com/facebook/facebook-python-business-sdk for the facebook business api

### Direct Calling
- It can be more complex to handle things manually.
- Promotes a better understanding of the API
- Slower but more effective integration
- Fuller control

## Rate Limits
Rate limits are restrictions on how many times you can make requests over a period of time on a given platform. Designed to reduces opportunities for abuse, control access and facilitate fare access for users. It's also a revenue source for the big platforms. They can vary across various access tiers like on X/Twitter.

### Twitter
https://docs.x.com/x-api/fundamentals/rate-limits

### Facebook
https://developers.facebook.com/docs/graph-api/overview/rate-limiting/

### LinkedIn
https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits


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

  

5. Demonstration

## Twitter

- Micro blogging site.

- 330 million active users.

- Real-Time updates for events

- Hashtag Driven Threads

  

1. Features:

- Tweets: 280-character text posts. Can include pictures and video

- Hashtags: Grouping content

- Trending Topics: Regional based topics with high level of engagement

- Twitter Ads: Promote Tweets and accounts

2. Business Opportunities:

- Posting tweets and reposting.

- Monitoring Tweets, Mentions, Hashtags.

- Analyzing posts' performance. Metrics like reposts/retweets, comments.

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

  

## WhatsApp:

  

Messaging platform with over 2 billion monthly active users.

  

Used for personal communication and business messaging.

  

Secure end-to-end encryption.

  

1. Features:

  

- WhatsApp Business API: Automate and manage business conversations.

  

- WhatsApp Cloud API: Meta-hosted version of WhatsApp API.

  

- Interactive Messages: Quick replies and buttons.

  

- Message Templates: Pre-approved messages for customer interactions.

  

2. Business Opportunities:

  

- Customer Support & Engagement.

  

- Automated Messaging & Chatbots.

  

- Transactional Messages (Order Confirmations, OTPs, etc.).

  

3. SDK:

  

- Installation

  

```

pip install twilio

```

  

- Sending a WhatsApp Message

  

```

from twilio.rest import Client

  

account_sid = 'YOUR_ACCOUNT_SID'

auth_token = 'YOUR_AUTH_TOKEN'

client = Client(account_sid, auth_token)

  

message = client.messages.create(

from_='whatsapp:+14155238886', # Twilio sandbox number

body='Hello, WhatsApp!',

to='whatsapp:+1234567890' # Your recipient number

)

  

print(message.sid)

```

  

4. Meta Platform (Recommended)

  

- Create a Meta Developer Account at Meta for Developers.

  

- Create a New App

  

- Set Up WhatsApp API, navigate to "Add a Product" → "WhatsApp" → "Set Up." Create or link a business account. Generate a test phone number for initial testing.

  

Provide basic app details and confirm.

  

- Set Up WhatsApp API:

  
  

Configure Webhook & Tokens:

  

Set up webhook callbacks to handle incoming messages.

  

Use the access token for API requests.

  

Submit for Review:

  

To send messages beyond testing, verify your business and get approval from Meta.

  

5. Case Study:

  

A restaurant wants to automate booking confirmations and daily specials via WhatsApp.

  

## Creating and Managing Apps On Meta

  

- Setting Up Meta App & Review Process:

  

1. Create an App on Meta Developer Portal:

  

2. Click "Create App" and select an app type (Business, Consumer, Gaming, etc.).

  

3. Add Products: Facebook Graph API, Instagram API, or WhatsApp Business API.

  

4. Setup Webhooks: Receive real-time updates.

  

## Review Process:

  

- Meta reviewes apps for compliance before going live. Each Permission as its own wizard for setting up application.

  

- Submit permissions and features for approval.

  

- Provide a detailed explanation and video demo of how the app uses requested permissions.

## Further Reading
https://developers.facebook.com/docs/
https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/
https://developer.x.com/en/docs/x-api
https://developers.facebook.com/docs/development/create-an-app/
https://developers.facebook.com/tools/
https://developers.facebook.com/docs/graph-api/webhooks/
https://developers.facebook.com/docs/whatsapp/cloud-api/
https://www.analyticsvidhya.com/blog/2021/10/sentiment-analysis-with-textblob-and-vader/
https://learn.microsoft.com/en-us/linkedin/
https://www.tweepy.org/
https://developers.facebook.com/docs/business-sdk/

## Code Examples
https://github.com/tinomhishi/Social-Media-Integrations-Workshop