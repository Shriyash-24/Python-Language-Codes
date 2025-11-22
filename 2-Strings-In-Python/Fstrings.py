name = "John"
age = 20
language = "Python"
hours = 3

# John is 20 years old.
print(name, "is", age, "years old.")

# John is 20 years old. He studies Python 3 hours a day.
print(name, "is", age, "years old. He studies", language, hours, "hours a day." )

# If we have variables like and want to write paragraphs then it will be clumsy and hectic.

 # Using f-string.
print(f"{name} is {age} years old. He studies {language} {hours} a day.")

sub1 = 78
sub2 = 87
sub3 = 83

print(f"{name} scored {sub1+sub2+sub3} marks in the exam.")
percent = (sub1+sub2+sub3)/3
print(f"{name} got {percent:.2f}% in the exam.")














