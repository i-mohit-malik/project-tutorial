import json
json_string='''{
    "students": [
        {"id": 1,
        "name": "Tim",
        "age": 21,
        "full-time": true
        },
        {"id": 2,
        "name": "Joe",
        "age": 33,
        "full-time": false
        } 
    ]
}'''

data = json.loads(json_string) #s in the end of load is because we are handlins a string

if __name__=="__main__":
    print(type(data))
    print(data)
    print(data['students'])
    print(data['students'][0])
    print(data['students'][0]['name'])