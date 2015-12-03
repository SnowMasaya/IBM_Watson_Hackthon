import json
from os.path import join, dirname
from argparse import ArgumentParser
import subprocess
import sys
model_path = (subprocess.check_output("echo $Watson_mdel", stderr=subprocess.STDOUT, shell=True)).decode('utf-8').strip() 
sys.path.append(model_path)
from model_search_list import ModelSearchList


class ExtractTextApi():

    def __init__(self):
        self.modelSearchList = ModelSearchList()
        self.text_data = []
        self.target_label = []
        self.predict_data = []

    def parse_args(self):

        p = ArgumentParser(description='Encoder-decoder neural machine trainslation')
        p.add_argument('target_data', help='[in] target_data')
        p.add_argument('predict_data', help='[in] predict_data')
        p.add_argument('text_data', help='[in] text_data')
        args = p.parse_args()

        return args

    def extract_missing_data(self, args):
        for line in open(args.target_data, "r"):
            self.target_data = line.strip().replace("[", "").replace("]", "").split(",")
            self.target_data = [int(x) for x in self.target_data] 
        for line in open(args.predict_data, "r"):
            self.predict_data = line.strip().replace("[", "").replace("]", "").split(",")
            self.predict_data = [int(x) for x in self.predict_data] 
        for line in open(args.text_data, "r"):
            text_data = line.strip().split(",")
            self.text_data.append(text_data[0])

        print("target label,predict label,text")
        for i in range(len(self.predict_data)): 
            if self.target_data[i] != self.predict_data[i]:
                print(self.modelSearchList.search_char_dictionary[self.target_data[i]]+ ",", end="")
                print(self.modelSearchList.search_char_dictionary[self.predict_data[i]]+ ",", end ="")
                print(self.text_data[i])

if __name__ == "__main__":
    extract_text_api = ExtractTextApi()
    args = extract_text_api.parse_args()
    extract_text_api.extract_missing_data(args)
