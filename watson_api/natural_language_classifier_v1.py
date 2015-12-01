import json
from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier
from watson_key import watson_key
import subprocess


class Watson_api():

    def __init__(self):
        self.watson_crediantial = watson_key()
        self.natural_language_classifier = NaturalLanguageClassifier(username=self.watson_crediantial.username,
                                                                     password=self.watson_crediantial.password)
        #print(json.dumps(self.natural_language_classifier.list(), indent=2))

    def train(self):
        # create a classifier
        with open('../resources/weather_data_train.csv', 'rb') as training_data:
             print(json.dumps(self.natural_language_classifier.create(training_data=training_data, name='weather2'), indent=2))

    def predict(self):
        # replace 47C164-nlc-243 with your classifier id
        status = self.natural_language_classifier.status(self.watson_crediantial.classifier_id)
        #print (json.dumps(status, indent=2, ensure_ascii=False))
        classes = self.natural_language_classifier.classify(self.watson_crediantial.classifier_id, 'RT @VJPtruelies: 劇場が削除される・新SRは一年に一度・ﾌﾞﾘｯﾂｪﾝの方が人気・ﾌﾞﾘｯﾂｪﾝの方がSR出演数上・CVなし。50位にも入れず、回では全く触れられない・劇場のオチが全く同じで使い回し・12/2…')
        print(classes["classes"][0])
        #print(json.dumps(classes, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    watson_api = Watson_api()
    watson_api.predict()
