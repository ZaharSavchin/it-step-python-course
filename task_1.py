import json

dict_of_data = {
    "name": "Micke",
    "age": 26,
    "hobbies": ["golf", "socker", "sleep"],
    "parents": {"father": {"name": "Bob", "age": 67},
                "mother": {"name": "Nadya", "age": 65}
                }
}

json_data = json.dumps(dict_of_data)
print(type(json_data))
# print(json_data)

with open('data/output.json', 'w') as file:
    json.dump(dict_of_data, file)

with open('data/output.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))