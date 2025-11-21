"""
When all the length of the sides of the triangle is known - a,b,c
Semi Perimeter (S) - ( a + b + c ) / 2
Area = square root of (s * (s-a) * (s-b) * (s-c))
"""
a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))
c = float(input("Enter the side C: "))
s = (a + b + c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("The area of the triangle is ", round(area, 2))
