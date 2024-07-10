import json 

import os

def append_json(file_path,data):
    if os.path.exists(file_path):
        
        with open(file_path,"a+",encoding='utf-8') as file:
                
                
                json.dump(data,file)
                file.write("\n")



    else:
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(data,file)

