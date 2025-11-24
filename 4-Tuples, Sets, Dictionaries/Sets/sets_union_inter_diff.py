student1 = {"English", "Maths", "CS", "Chemistry","Physics"}
student2 = {"English", "Biology", "Chemistry","Physics"}

print(student1, type(student1)) # {'Physics', 'English', 'CS', 'Chemistry', 'Maths'} <class 'set'>
print(student2, type(student2)) # {'Physics', 'Chemistry', 'English', 'Biology'} <class 'set'>

# Common Subjects Of student1 and student2 ~ INTERSECTION
common_subjects = student1.intersection(student2)
print(common_subjects) # {'Chemistry', 'English', 'Physics'}
common_subjects = student1 & student2 # Another way of using intersection
print(common_subjects) # {'Chemistry', 'English', 'Physics'}

# All the subjects
all_subjects = student1.union(student2)
print(all_subjects) # {'Chemistry', 'English', 'Physics', 'Maths', 'Biology', 'CS'}

student3 = {"Sanskrit", "Maths", "Hindi"}
all_subjects = student1.union(student2,student3)
print(all_subjects) # {'Sanskrit', 'Maths', 'CS', 'Chemistry', 'Biology', 'Hindi', 'Physics', 'English'}
common_subjects = student1.intersection(student2,student3)
print(common_subjects) # set() ~ Empty Set

all_subjects = student1 | student2 | student3 # Another way of using union
print(all_subjects) # {'Maths', 'Sanskrit', 'Physics', 'English', 'CS', 'Chemistry', 'Hindi', 'Biology'}

days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
weekends = {"Saturday", "Sunday"}

# Difference Of Sets
weekdays = days - weekends # elements of days which are not in weekends
print(weekdays) # {'Thursday' , 'Friday', 'Monday', 'Tuesday', 'Wednesday'}

weekdays = days.difference(weekends)
print(weekdays) # {'Monday', 'Thursday', 'Friday', 'Tuesday', 'Wednesday'}
