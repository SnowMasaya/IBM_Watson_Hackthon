import json
from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier
from watson_key import watson_key
from argparse import ArgumentParser
import subprocess
import sys
model_path = (subprocess.check_output("echo $Watson_mdel", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
sys.path.append(model_path)
from model_search_list import ModelSearchList
from sklearn.metrics import f1_score


class Watson_api():

    def __init__(self):
        self.fname = "" 
        self.modelSearchList = ModelSearchList()
        self.text_data = []
        self.target_label = []
        self.watson_crediantial = watson_key()
        self.watson_classifier = self.watson_crediantial.classifier_twitter_hash_classfier
        self.natural_language_classifier = NaturalLanguageClassifier(username=self.watson_crediantial.username,
                                                                     password=self.watson_crediantial.password)
        #print(json.dumps(self.natural_language_classifier.list(), indent=2))

    def parse_args(self):

        p = ArgumentParser(description='Encoder-decoder neural machine trainslation')
        p.add_argument('data', help='[in] data')
        args = p.parse_args()

        return args

    def __read_data(self):
        for line in open(self.fname, "r"):
            split_line = line.split(",")
            self.text_data.append(split_line[0].strip())
            self.target_label.append(self.modelSearchList.search_dictionary[split_line[1].strip()])

if __name__ == "__main__":
    watson_api = Watson_api()
    args = watson_api.parse_args()
    watson_api.predict(args)
