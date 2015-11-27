#!/usr/bin/python3

from twitter import *
from twitter_key import twitter_key

twitter_auth = twitter_key()
t = Twitter(auth=OAuth(twitter_auth.token, twitter_auth.token_key, twitter_auth.con_secret, twitter_auth.con_secret_key))
data = t.search.tweets(q="#python", count=100)

for i in range(len(data["statuses"])):
    print(data["statuses"][i]["text"], end='')
    print("," + data["statuses"][i]["entities"]["hashtags"][0]["text"])
