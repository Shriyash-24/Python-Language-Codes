"""
Simple Interest = PRT / 100
P - Principal
R - Rate
T - Time
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))
si = ( principal * rate * time ) / 100
print("Simple Interest = ", si)