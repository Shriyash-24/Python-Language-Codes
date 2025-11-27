# When we want to store high level data types, like lists, tuple, dictionaries.. and when we want to store these in..
# memory.. then we must convert into sequence of bytes so computer can understand ~ Serialization
# And then it must be converted back and that is known as De-serailization.
import pickle
students = {'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 71.0}}


print(students) # Entire dictionary
print(type(students)) # <class 'dict'>

with open('students_info.txt', 'wt') as fh:
    # fh.write(students) - Error because write takes string only, not dictionary.
    fh.write(str(students))


# After saving the data, we can try to read the content.
with open("students_info.txt", "rt") as fh:
    content = fh.read()

print(content)
print(type(content)) # <class 'str>

'''
out = dict(content)
print(out) # ERROR, because we still can't access the file.. because content is in string and can't be converted.
'''

# Serialization using pickle module.
students = {'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.5},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 71.0}}

with open("stu.bin", "bx") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization ~ Reading back the data from the binary file.
with open("stu.bin", 'rb') as fh:

    data1 = pickle.load(fh)
    print(data1) # {'roll': 101, 'name': 'John', 'percent': 78.5}
    print(type(data1)) # <class 'dict'>

# We can use the while loop to load all the data as well while handling the EOF error and breaking it.

