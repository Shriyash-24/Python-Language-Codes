"""
Simple arithmetic module: elevena.py
"""

def add(num1,num2):
    return num1+num2

def square_root(num):
    return num ** 0.5

# __name__ variable
a = 10
b = 20
result = add(a,b)
print(result) # Now this will run in 11b-mycode.py as well if I import the full module.

# So, __name__ variable is a special variable that allows us to write executable code in the module.
if __name__ == "__main__":
    a = 10
    b = 20
    result = add(a,b)
    print(result)
