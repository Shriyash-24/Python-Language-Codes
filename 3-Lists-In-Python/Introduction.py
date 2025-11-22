name = "John"
age = 20
percent = 85.5

student = ["John", 20, 85.5]
print(type(student)) # <class 'list'>
print(student) # ['John', 20, 85.5]

# Lists are ordered always.

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[0])
print(days_of_week[4])
print(f"Last day of the week is {days_of_week[-1]}")

print(len(days_of_week)) # Length
print(days_of_week[8]) # Error
