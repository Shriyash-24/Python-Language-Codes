# JSON - JavaScript Object Notation, Used in many programming languages. Widely accepted.
import json

students = {'s1': {'roll': 101, 'name': 'John', 'percent': 98.5, 'sports': False},
            's2': {'roll': 102, 'name': 'Carol', 'percent': 92.5, 'sports': False},
            's3': {'roll': 103, 'name': 'Alice', 'percent': 81.5, 'sports': True}}

print(students) # {'s1': {'roll': 101, 'name': 'John', 'percent': 98.5}, 's2': {'roll': 102, 'name': 'Carol', 'percent': 92.5}, 's3': {'roll': 103, 'name': 'Alice', 'percent': 81.5}}
print(type(students)) # <class 'dict'>

# dump() - Write a content using json
'''
with open("student_data.json", "w") as fh:
    json.dump(students, fh, indent=4)

# Beautifully writes dictionary in json format.
'''

'''
# load()
with open("student_data.json", "r") as fh:
    data = json.load(fh)

print(data) # {'s1': {'roll': 101, 'name': 'John', 'percent': 98.5, 'sports': True}, 's2': {'roll': 102, 'name': 'Carol', 'percent': 92.5, 'sports': False}, 's3': {'roll': 103, 'name': 'Alice', 'percent': 81.5, 'sports': True}}
print(type(data)) # <class 'dict'>
'''

# dump() is used for serailization, load() for deserializarion.

# update() - Helps to add new data.
# Step 1 - Read the old data.
with open("student_data.json", "r") as fh:
    data = json.load(fh)

# make changes in students dictionary
data.update(students)
# dump - Write updated data in the JSON file.
with open("student_data.json", "w") as fh:
    json.dump(data, fh, indent=4)


