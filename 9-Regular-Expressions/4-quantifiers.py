# Quantifiers are symbols, used for quantity.

# +, *, ?,
import re
message = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10."

# [a-z][a-z][a-z][a-z] = [a-z]{4}
pat = r"[a-z]{4}"
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(4, 8), match='curr'>

# [A-Z][a-z][a-z][a-z][a-z][a-z] = [A-Z][a-z]{5}
pat = r"[A-Z][a-z]{5}"
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(12, 18), match='Python'>

pat = r"[A-Z][a-z]{2,5}" # [a-z] atleast 2 and maximum 5.
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(0, 3), match='The'>

# + ==> matches 1 or more repetitions of the previous pattern.
pat = r"[A-Z][a-z]+" # 1 or more..
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(0, 3), match='The'>

# ? ==> 0 or 1 repetitions of the previous pattern.
pat = r"[A-Z][a-z]?"
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(0, 2), match='Th'>

# * ==> 0 or more.
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, message)
print(match_obj) # <re.Match object; span=(0, 3), match='The'>


















