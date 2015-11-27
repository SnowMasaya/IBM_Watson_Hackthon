#!/usr/bin/python3

from twitter import *
import subprocess

token = (subprocess.check_output("echo $Twitter_Access_Token", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
token_key = (subprocess.check_output("echo $Twitter_Access_Token_Sercert", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
con_secret = (subprocess.check_output("echo $Twitter_Consumer_Key", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
con_secret_key = (subprocess.check_output("echo $Twitter_Consumer_Sercert", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
print(con_secret)
print(con_secret_key)

t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))
data = t.search.tweets(q="#python")
