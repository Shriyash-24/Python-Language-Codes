"""
If marks >= 60. student is pass else student is fail and
the student is pass then we print the grade
>= 90 - Grade A
80 - 89 - Grade B
70 - 79 - Grade C
60 - 69 - Grade D
"""

marks = float(input("Enter marks: "))
if marks >= 60:
    print("Congrats, you passed.")
    if marks >= 90:
        print("Grade A")
    elif marks >= 80 and marks < 90:
        print("Grade B")
    elif marks >= 70 and marks < 80:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You failed, study hard next time.")
