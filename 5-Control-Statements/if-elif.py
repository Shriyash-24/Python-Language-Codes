"""
>= 90 - Grade A
80 to 89 - B
70 TO 79 - C
60 To 69 - D
< 60 - E
"""
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Grade E")
