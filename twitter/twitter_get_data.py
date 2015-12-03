#!/usr/bin/python3

from twitter import *
from twitter_key import twitter_key
from model_search_list import ModelSearchList

twitter_auth = twitter_key()
t = Twitter(auth=OAuth(twitter_auth.token, twitter_auth.token_key, twitter_auth.con_secret, twitter_auth.con_secret_key))

modelSearchList = ModelSearchList()
f = open("twitter_label_count.txt", "w")

for item in modelSearchList.search_list:
#for item in modelSearchList.search_list_test:
    data = t.search.tweets(q=item, count=400)
    f.write(str(len(data["statuses"])) +","+ item + "\n")
    for i in range(len(data["statuses"])):
        out_data = data["statuses"][i]["text"].replace("\n", "").replace(",", "") 
        print(out_data, end='')
        print("," + item) 
        #print("," + data["statuses"][i]["entities"]["hashtags"][0]["text"])
f.close()
