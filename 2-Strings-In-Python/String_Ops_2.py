# Counting substrings from a string - count()
# Syntax - string.count(substring)

s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(s1.count(s2)) # 2
print(f"Occurrences of {s2} is {s1.count(s2)}")
s3 = "e"
print(s1.count(s3)) # 3
s4 = "learn"
print(s1.count(s4)) # 1

# Cases of string - upper(), lower(), title(), captitalize()
c1 = "We are learning Python"
print(c1.upper())  # WE ARE LEARNING PYTHON
print(c1.lower()) # we are learning python
print(c1.title()) # We Are Learning Python
print(c1.capitalize()) # We are learning python

# Starting and ending of string
print(c1.startswith("W")) # T
print(c1.startswith("We")) # T
print(c1.startswith("We are")) # T
print(c1.startswith("are")) # F
print(c1.startswith("we")) # F

print(c1.endswith("Python")) # T
print(c1.endswith("n")) # T
print(c1.endswith("Pytho")) # F


