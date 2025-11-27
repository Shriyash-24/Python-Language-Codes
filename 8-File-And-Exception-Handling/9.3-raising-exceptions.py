# raise

salary = float(input("Enter salary: "))
if salary < 0:
    raise ValueError("Salary cannot be negative")
else:
    print(f"Your salary is {salary}")

# When salary was negative, we are using raise to throw an error.

age = float(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print(f"Your age is {age}")

# You can raise generic exception

age = float(input("Enter your age: "))
if age < 0:
    raise Exception("Age cannot be negative")
else:
    print(f"Your age is {age}")
