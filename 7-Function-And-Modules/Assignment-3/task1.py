"""
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

Expected Output:
For example, if the function is called with 5, it should return:

"""
# USING LOOP
def factorial_l(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n - 1
    return factorial
fact_num = int(input("Enter a number: "))
print(f"Factorial of {fact_num} is: {factorial_l(fact_num)}")

# RECURSION WAY
def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n-1)

fact_num = int(input("Enter a number: "))
print(f"Factorial of {fact_num} is: {factorial_r(fact_num)}")