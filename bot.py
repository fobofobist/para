import os
import tweepy

# Get credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Function to reply to tweets
def reply_to_tweets():
    keyword = "link"
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(10)
    for tweet in tweets:
        try:
            reply_text = f"Hey @{tweet.user.screen_name}, here is a reply to your tweet!"
            api.update_status(reply_text, in_reply_to_status_id=tweet.id)
            print(f"Replied to: {tweet.user.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error: {e}")

# Run the bot
reply_to_tweets()
