import json
import re

def clean_data(file_name):

    with open(file_name, encoding='utf-8') as f:
        data = json.load(f)

    de_duplicated = []
    for dic in data:
        if dic not in de_duplicated:
            de_duplicated.append(dic)

    for dic in de_duplicated:
        dic['current_price'] = '$' + str(int(dic['current_price']) / 100)
        num_pattern = "\d\d+%"
        text_pattern = ""
        if dic['rating'] and re.search(num_pattern, dic['rating']):
            dic['num_score'] = re.search(num_pattern, dic['rating']).group(0)
            dic['word_score'] = None
        else:
            dic['num_score'] = None
            dic['word_score'] = None


        print(dic['num_score'])


clean_data('test2.json')

