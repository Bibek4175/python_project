import json 
from collections import defaultdict
import os

def append_json(file_path,value,key):
    data = defaultdict(list)
    if os.path.exists(file_path):
        with open(file_path,"r",encoding='utf-8') as file:

            data = json.load(file)

    data[key].append(value)

    with open(file_path,"w",encoding = 'utf-8') as file:
        json.dump(data,file)


