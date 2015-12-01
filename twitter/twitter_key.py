#!/usr/bin/python3
__author__ = 'ohgushimasaya'
import subprocess


class twitter_key():

    def __init__(self):
        self.token = (subprocess.check_output("echo $Twitter_Access_Token", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.token_key = (subprocess.check_output("echo $Twitter_Access_Token_Sercert", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.con_secret = (subprocess.check_output("echo $Twitter_Consumer_Key", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.con_secret_key = (subprocess.check_output("echo $Twitter_Consumer_Sercert", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
