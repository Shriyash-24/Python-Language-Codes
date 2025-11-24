s1 = "Hello World"
for char in s1:
    print(char)
# O/P -
# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d

employee = {'empid':1001, 'name': "John Gray", 'dependent': "HR"}
for i in employee:
    print(i)
# O/P -
# empid
# name
# dependent

# It only outputs the keys.
# How to print values?

for i in employee:
    print(i, employee[i])
# O/P -
# empid 1001
# name John Gray
# dependent HR

print(employee.items()) # dict_items([('empid', 1001), ('name', 'John Gray'), ('dependent', 'HR')])

for i in employee.items():
    print(i)
# O/P -
# ('empid', 1001)
# ('name', 'John Gray')
# ('dependent', 'HR')

for i in employee.items():
    print(i[0])
# O/P -
# empid
# name
# dependent

for i in employee.items():
    print(i[1])
# O/P -
# 1001
# John Gray
# HR

for i in employee.items():
    print(i[0], i[1])
# O/P -
# empid 1001
# name John Gray
# dependent HR

