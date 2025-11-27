import pickle

students = {'s1': {'roll': 101, 'name': 'John', 'percent': 78.5},
            's2': {'roll': 102, 'name': 'Carol', 'percent': 92.5},
            's3': {'roll': 103, 'name': 'Alice', 'percent': 81.5}}

print(students) # {'s1': {'roll': 101, 'name': 'John', 'percent': 78.5}, 's2': {'roll': 102, 'name': 'Carol', 'percent': 92.5}, 's3': {'roll': 103, 'name': 'Alice', 'percent': 81.5}}
print(type(students)) # <class 'dict'>

# Serialization
with open("students.bin", "bw") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserailization
'''
with open("students.bin", "rb") as fh:
    while True:
        try:
            data1 = pickle.load(fh)
            print(data1, type(data1))  # 'roll': 101, 'name': 'John', 'percent': 78.5} <class 'dict'>
        except EOFError:
            print("Prints data 3 times..")
            break
'''
# Print the names of the students who secured 90 or more percent.
'''
with open("students.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh) # Full dictionary loaded.
            if data['percent'] >= 90:
                print(data['name'])
        except EOFError:
            print("Done")
            break
'''

# Print the names as a list..
student_list_90 = []
with open("students.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] >= 90:
                student_list_90.append(data['name'])
        except EOFError:
            print("Done")
            break

print(f"List of students who secured 90 or more: {student_list_90}")

