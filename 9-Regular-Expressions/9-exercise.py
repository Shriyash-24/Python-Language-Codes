import re

with open("student_details", "rt") as fh:
    data = fh.read()

pattern = r"[a-zA-Z0-9_.-]+[@][a-z]+[.][a-z]+"
match_obj = re.finditer(pattern, data)

for matches in match_obj:
    print(matches)

# I get valid and invalid emails.
pattern = r"[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-z]+[.][a-z]+"
pattern2 = r"[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+"
match_obj = re.finditer(pattern2, data)
for matches in match_obj:
    print(matches) # it prints correct emails but also prints abc@example.com.. as it ignores _123 in the start from invalid email.

pattern3 = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
match_obj = re.finditer(pattern3, data)
for matches in match_obj:
    print(matches) # Valid emails only.