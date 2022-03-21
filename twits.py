#!/usr/bin/env python3
"""Tweet Consumer App """
import tweepy
import config


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    me = client.get_me(user_fields=["public_metrics"])
    print(f"User name: {me.data.name}")
    print(f"User handle: {me.data.username}")
    print(f"User followers count: {me.data.public_metrics['followers_count']}")


def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    """Returns a list og latest ZTM tweets"""
    ztm = client.get_user(username='zerotomasteryio')
    response = client.get_users_tweets(ztm.data.id,)
    return response.data


if __name__ == '__main__':
    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_token=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_SECRET
    )
    print("==========================ABOUT ME=========================")
    about_me(client)
    print("Tweets")
    for tweet in get_ztm_tweets(client):
        print(tweet, end="\n\n")
