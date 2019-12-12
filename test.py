import json
import pandas as pd
from predict import Predictor
def get_string(x):
        now = x.split('\n')
        o = now[1].split(' ')
        while '' in o:
            o.remove('')
        return o[1]

with open("config/msraner_config.json", "r") as fr:
    config = json.load(fr)

predictor = Predictor(config)

tests = pd.read_csv('Test.csv')
with open('output.txt', 'w', encoding='utf-8') as o:
    #o.write('id,aspect,opinion\n')
    for ids in range(1, 2235):
        input_str = get_string(str(tests.loc[ids-1:ids-1, ['Review']]))
        index = int(get_string(str(tests.loc[ids-1:ids-1, ['id']])))
        text = []
        for key in input_str:
            text.append(key)
        chunks = predictor.predict(text)
        entities = []
        for chunk in chunks:
            entity_name, start, end = chunk
            entity = "".join(text[start - 1: end])
            entities.append({'start':start, 'end':end, 'word':entity, 'type':entity_name})
        entities = sorted(entities, key=lambda x: x['start'])
        #print(str(index) + "  " + input_str + " " +str(len(entities)))
        for entity in entities:
            #print(entity)
            o.write(str(index)+','+entity['type'] +',' + entity['word']+'\n')