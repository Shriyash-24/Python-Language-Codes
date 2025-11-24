# Normal Way
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# true-expression if condition else false-expression
print("Even") if num % 2 == 0 else print("Odd")