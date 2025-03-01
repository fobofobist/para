import os
import tweepy

# Get credentials from environment variables
API_KEY = os.getenv("989253d8826582500506eec37e3a7ab2")
API_SECRET = os.getenv("a1ced770cff6252505d17325c9c54baf")
ACCESS_TOKEN = os.getenv("0c1e8bac81037bff42488388c8998e2d")
ACCESS_SECRET = os.getenv("50e844b1de1872b3dd199032b21ffa25")

# Authenticate with Twitter AAAAAAAAAAAAAAAAAAAAAFCYzgEAAAAAQuHovv2oU7DuEVkYKlWs%2F6Alv7k%3DUk3u37SNwrSxbcp8b03gCLdWOLJneY7s19zajR8VtIJTff6NvK
auth = tweepy.OAuthHandler(UTqKtNROvu2BiM6OFlHpCmmxy, 3YvggsZZIsxXnzbNYeAMOjtw5BYJDcUqiSWV8j8S9yn74M9yNj)
auth.set_access_token(1882142905638268928-GlgM44bDRUvqQxH0BBq2blJm8H4hZd, mW0cY5qlMzSDoY3bLfKu20gwwQmstePGzik4kM077NcaB)
api = tweepy.API(auth)

# Function to reply to tweets
def reply_to_tweets():
    keyword = "link"
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(10)
    for tweet in tweets:
        try:
            reply_text = f"@{tweet.user.screen_name} https://ay.live/1Kpa!"
            api.update_status(reply_text, in_reply_to_status_id=tweet.id)
            print(f"Replied to: {tweet.user.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error: {e}")

# Run the bot
reply_to_tweets()
