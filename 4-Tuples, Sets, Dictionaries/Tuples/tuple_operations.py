# Tuple Concatenation - '+'
student_detail1 = (1001,"John")
student_detail2 = (78.5,91.0,83.5,79.5)
student_details = student_detail1 + student_detail2
print(student_details) # (1001, 'John', 78.5, 91.0, 83.5, 79.5)

# Repetition - '*'
t1 = ("Class 5", 5000)
print(t1 * 3) # ('Class 5', 5000, 'Class 5', 5000, 'Class 5', 5000)

# Membership - in, not in
print(91.0 in student_detail2) # T
print(99.0 in student_detail2) # F
print(86.0 not in student_detail2) # T
print(91.0 not in student_detail2) # F

# Slicing in Tuples

t2 = (1,2,"Hello",True,None,"Python",23,24,False)
print(t2[1:6:2]) # (2, True, 'Python')
print(t2[4::2]) # (None, 23, False)
