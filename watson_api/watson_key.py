#!/usr/bin/python3
__author__ = 'ohgushimasaya'
import subprocess


class watson_key():

    def __init__(self):
        self.classifier_twitter_hash_classfier = (subprocess.check_output("echo $Watson_twitter_hash_classfier", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.classifier_twitter_keyword_classfier = (subprocess.check_output("echo $Watson_twitter_keyword_classfier", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.classifier_twitter_unblance_keyword_classfier = (subprocess.check_output("echo $Watson_twitter_keyword_unblance_classfier", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.twitter_category_classfier = (subprocess.check_output("echo $Watson_twitter_category_classfier", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.twitter_priority_classfier = (subprocess.check_output("echo $Watson_twitter_priority_classfier", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.username = (subprocess.check_output("echo $Watson_username_v2", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.password = (subprocess.check_output("echo $Watson_password_v2", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
