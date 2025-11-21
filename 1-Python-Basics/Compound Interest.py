"""
Amount = P(1 + R/100) ** t
CI = Amount - Principal
"""

principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))
## amount1 = principal * (1 + rate / 100) ** time
amount2 = principal * pow((1 + rate / 100),time)
ci = amount2 - principal
print("Compound Interest = ", round(ci))
