# A function calls itself till a certain condition is not met.
# Factorial of n => n * (n-1) * (n-2).. 2 * 1
# n! ~ 4! = 4 * 3 * 2 * 1 = 24

# Without Recursion
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial

n = 5
print(f"Factorial of {n} is {fact(n)}") # Factorial of 5 is 120

# With Recursiom ~ 2 Parts to any recursive functioon.
"""
1. Base/Terminal Condition
2. Recursive condition
"""

# n! = n * (n-1)!
# Base - 1

def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact_rec(num-1)
        return factorial

print(fact_rec(4)) # 24
# Working..
"""
fact_rect(4) -- 4 * fact_rec(3)
fact_rect(3) -- 3 * fact_rec(2)
fact_rect(2) -- 2 * fact_rec(1)
fact_rect(1) -- Returns 1
fact_rec(2) -- 2 * 1 = Returns 2
fact_rec(3) -- 3 * 2 = Returns 6
fact_rect(4) -- 4 * 6 = Returns 24
24 is the answer!
Calculation will not start until the base condition is reached.
"""


