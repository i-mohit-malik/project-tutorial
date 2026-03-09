import json

with open("file.json","r") as f:
    data =json.load(f)
    
if __name__=="__main__":
    print(type(data))
    print(data.items())
    print(data)