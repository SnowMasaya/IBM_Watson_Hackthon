# -*- coding: utf-8 -*-

import os
import sys


CATEGORY_DIR = './category'
PRIORITY_DIR = './priority'
INPUT_DIR = './data'

for file_name in os.listdir(INPUT_DIR):

    if not file_name.endswith('.csv'):
        continue

    category, extn = file_name.split('.')
    category_output = []
    priority_output = []

    with open(INPUT_DIR + '/' + file_name, 'rb') as f:
        for line in f:
            items = line.split(',')
            text = ''.join(items[:-1])
            priority = items[-1].strip()

            if priority not in ['High', 'Middle', 'Low']:
                print items[0]
                print("filename: %s" % file_name)
                print("priority: %s" % priority)
                raise Exception('Priority text is invalid!')
                sys.exit(-1)

            if priority == 'High':
                category_save_txt = text + ',' + category
                category_output.append(category_save_txt)
            priority_save_txt = text + ',' + priority
            priority_output.append(priority_save_txt)
    
    with open('%s/%s_cat.csv' % (CATEGORY_DIR, category), 'wb') as f:
        f.write('\n'.join(category_output))
    with open('%s/%s_pri.csv' % (PRIORITY_DIR, category), 'wb') as f:
        f.write('\n'.join(priority_output))
