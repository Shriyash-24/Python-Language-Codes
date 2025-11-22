s1 = "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "3.14"
print(language + version) # Concatenation
# Subtraction doesn't work.

s2 = "Python"
print(s2*3) # '*' is repetition operator.

# Membership Operator
print("Python" in s1) # T
print("z" in s1) # F
print("z" not in s1) # T
print("Python" not in s1) # F

# Comparison of strings
print("Python" == "Python") # T
print("Python " == "Python") # F

# Removing spaces from string --> strip()
s1 = "Python "
s2 = s1.strip()
print(s2)

s4 = "         Python           "
s5 = s4.strip()
print(s5)

# Replace() - Doesn't change the current string, just produces a new output. By defualt replaces everything. That's why
# count should be used.
s6 = "We are learning Python"
print(s6.replace("Python", "Java"))
print(s6.replace("e", "E", 1))



