def add(a, b):
    return a+b

# Positional Arguments - passing arguments in the order of their position

result = add(10,5)
# 10 goes to a, 5 goes to b ~ So positional.

# Default arguments ` Assign default values.
def add(a, b=10):
    return a+b
# b is default value here.
result = add(20,5)
print(result) # 25

res2 = add(45)
print(res2) # 55 ( value of b is 10 )

# def add(a,b=11,c):
#     return a+b+c
# result = add(10,20, 30)
# print(result) # ERROR

# The non-default arguments should not follow default arguments.
def add(a,c,b=10):
    return a+c+b
result = add(10,20)
print(result) # 40

def add(a,b=10,c=10):
    return a+b+c
result = add(10) # Value passed to a only.
print(result)

# I want to give value of a and c only and want to keep b as default
# Named Arguments or Keyword Argument
result = add(10,c=50) # Keyword Argument
print(result) # 70

# We can change the order like this using keyword arguments.

# *args ~ N number of arguments or variable length arguments.
# *args ~ Variable length positional arguments (0 to n)
# * allows to have multiple values, args stores those.
def add(*args):
    print(args)

add(2,5) # (2, 5)
add(3,4,5,6) # (3, 4, 5, 6)

# Type of args is tuple.
def add(*args):
    return sum(args)
result = add(10,20,4,1,2,3,9)
print(result) # 49
result = add()
print(result) # 0

# I can use different names, such as *nums or something else but *args is the standard.

def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent")
    else:
        percent = sum(marks) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(1,"James", 87.0,69,5,81,5, 74,0)
student_details(2,"Carol", 91.0,49.5,84.0, 86.5)
student_details(3,"Mark", 81.5,83.5,79.0)
student_details(4,"Alice")

# Variable length keyword arguments - **kwargs
# ( 0 or more keyword arguments )
def func(**kwargs):
    print(kwargs)

func(x=10,y=20) # {'x': 10, 'y': 20}
func() # {}

# Datatype - Dictionary.

def student_details(sid,sname,**marks):
    if len(marks) == 0:
        print(f"{sname} did not attend exam.")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(101,"John", sub1 = 78.5, sub2 = 81.0, sub3 = 90.5) # John with id 101 secured 83.33333333333333%
student_details(102,"Mark", sub4 = 78.5, sub2 = 88.5, sub1 = 90.5, sub5 = 67.4) # Mark with id 102 secured 81.225%

# kwargs should come after every argument, not before.






