#!/usr/bin/python3
__author__ = 'ohgushimasaya'
import subprocess


class watson_key():

    def __init__(self):
        self.username = (subprocess.check_output("echo $Watson_username", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
        self.password = (subprocess.check_output("echo $Watson_password", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
