import json

# Python dictionary (can be list, dict, nested structures, etc.)
# data = {
#     "name": "Sekh",
#     "age": 28,
#     "skills": ["Python", "Django", "API"],
#     "is_active": True
# }

# # Write JSON to file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)  # indent=4 makes it pretty




# with open("data.json", "r") as f:
#     loaded_data = json.load(f)

# print(loaded_data)


import json

data = {"city": "Kolkata", "temp": 32}

# Convert Python dict → JSON string
json_str = json.dumps(data, indent=2)
print(json_str)

# Convert JSON string → Python dict
back_to_python = json.loads(json_str)
print(back_to_python)

'''
json.dump(obj, file)	Write Python object as JSON to file
json.dumps(obj)	Convert Python object → JSON string
json.load(file)	Read JSON from file → Python object
json.loads(string)	Convert JSON string → Python object
'''