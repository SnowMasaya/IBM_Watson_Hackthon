#!/usr/bin/python3
from pywatson.watson import Watson
from watson_key import watson_key

watson_crediantial = watson_key()
watson = Watson(url='https://gateway.watsonplatform.net/natural-language-classifier/api', username=watson_crediantial.username, password=watson_crediantial.password)
print(dir(watson))
