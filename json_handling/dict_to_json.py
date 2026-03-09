import json
from json_string import data

new_json=json.dumps(data, indent=2)

if __name__=="__main__":
    print(type(new_json)) #this is created in form of string
    print(new_json)
    
    with open("file2.json","w") as f:
        json.dump(data,f,indent=2) #this is created in form of new json file