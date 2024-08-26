import tweepy
import requests

from dotenv import load_dotenv
import os

load_dotenv()


def scrape_user_tweets(username, num_tweets=5, mock: bool = True):
    tweet_list = []

    if mock:
        EDEN_TWITTER_GIST = "https://gist.github.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/"
        tweets = requests.get(EDEN_TWITTER_GIST, timeout=10).json()

        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/{tweet["id"]}"
            tweet_list.append(tweet_dict)
    
    return tweet_list


if __name__ == "__main__":
    print("Get tweets")
    tweets = scrape_user_tweets(username="EdenEmarco177")
    print(tweets)
