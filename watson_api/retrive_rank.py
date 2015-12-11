import json
from os.path import join, dirname
import subprocess
import sys
model_path = (subprocess.check_output("echo $Watson_Retrive_Rank", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip()
sys.path.append(model_path)
from watson_developer_cloud.retrive_rank_v1 import RetriveRank
from watson_key import watson_key
from argparse import ArgumentParser
model_path = (subprocess.check_output("echo $Watson_model", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip()
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
        self.watson_classifier = self.watson_crediantial.twitter_category_classfier
        self.natural_language_classifier = NaturalLanguageClassifier(username=self.watson_crediantial.username,
                                                                     password=self.watson_crediantial.password)
        #print(json.dumps(self.natural_language_classifier.list(), indent=2))

    def parse_args(self):

        p = ArgumentParser(description='Encoder-decoder neural machine trainslation')
        p.add_argument('data', help='[in] data')
        args = p.parse_args()

        return args

    def train(self):
        # create a classifier
        with open('../resources/weather_data_train.csv', 'rb') as training_data:
             print(json.dumps(self.natural_language_classifier.create(training_data=training_data, name='weather2'), indent=2))
    
    def __read_data(self):
        for line in open(self.fname, "r"):
            split_line = line.split(",")
            self.text_data.append(split_line[0].strip())
            self.target_label.append(self.modelSearchList.search_category_dictionary[split_line[1].strip()])

    def predict(self, args):
        # replace 47C164-nlc-243 with your classifier id
        status = self.natural_language_classifier.status(self.watson_classifier)
        self.fname = args.data
        self.__read_data()
        predict_id = []
        #print (json.dumps(status, indent=2, ensure_ascii=False))
        for i in range(len(self.text_data)):
            classes = self.natural_language_classifier.classify(self.watson_classifier, self.text_data[i])
            class_id = self.modelSearchList.search_category_dictionary[classes["classes"][0]["class_name"].replace("\"", "").replace("\"", "")]
            predict_id.append(class_id)
        print(self.target_label)
        print(predict_id)
        f1_score_twitter = f1_score(self.target_label, predict_id, average='macro') 
        print("----F measure-----")
        print(f1_score_twitter)
        #print(json.dumps(classes, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    watson_api = Watson_api()
    args = watson_api.parse_args()
    #watson_api.predict(args)
