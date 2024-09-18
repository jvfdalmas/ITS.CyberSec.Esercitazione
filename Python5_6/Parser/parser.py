# A parser refers to a tool or library that reads JSON data and converts it into a format that Python can work with, typically dictionaries or lists.

import json
import jsonschema
import requests

def JsonSeriallize(data):
    with open("data_file.json", "w") as write:
        json.dump(data,write)

def JsonDeserialize(sFile):
    with open(sFile, "r") as read:
        return json.load(read)
    
def print_dict(dData):
    for key, value in dData.items():
        if type(value) == dict:
            print("key: ", key, "\n", "value: ", value, "\n", type(value), end="")
            print("\n")
            print_dict(value)
        else:
            print("key: ", key, "\n", "value: ", value, "\n", type(value), end="")
            print("\n")

data1 = JsonDeserialize("example_1.json")
data2 = JsonDeserialize("example_2.json")

print("example 1:\n")
print_dict(data1)

print("example 2:\n")
print_dict(data2)

# with open("OutputFile1.py", "w") as write:
#     json.dump(data1, write, indent=1)

# with open("OutputFile2.py", "w") as write:
#     json.dump(data2, write, indent=1)

print("\n")

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        }
    },
    "required": ["name"],
    "additionalProperties": False
}

#TEST SCHEMA:

instance1 = {"name":"Mario","age": 44, "scores": [12,33,44]}
instance2 = {"name":"Mario","age": "quarantaquattro", "scores": [12,33,44]}

for item in instance1, instance2:
    try:
        jsonschema.validate(item, schema)
        print("L'istanza è coerente con lo schema")
    except jsonschema.exceptions.ValidationError:
        print("L'istanza non è valida")

print("\n")

# api_url = "https://jsonplaceholder.typicode.com/todos/5"
api_url = "https://corriere.it"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])
if(response.status_code==200):
    if (type(response.json()) is dict):
        print_dict(response.json())