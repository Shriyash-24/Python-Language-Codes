import re
s1 = "Python is a programming language."
# [A-Z], [a-z]

pattern = r"old\new" # r here means raw string.
print(pattern) # old\new is printed and python doesn't check for  \n or something else.
pattern = r"[a-z][a-z]" # look for 2 consecutive lowercase characters.

match_object = re.search(pattern, s1)
print(match_object) # <re.Match object; span=(1, 3), match='yt'>

pat = r"[A-Z][a-z][a-z]"
match_object = re.search(pat, s1)
print(match_object) # <re.Match object; span=(1, 3), match='yt'>

# \d and \t
# \d matches 1 digit character. It is similar to [0-9]

s2 = "Python is a programming language. python3.14 is the current version."
pat = r"[a-z][a-z][a-z]\d"
match_object = re.search(pat, s2)
print(match_object) # <re.Match object; span=(37, 41), match='hon3'>

# \D matches 1 non-dgit character.
pat = r"[a-z][a-z][a-z]\D"
match_object = re.search(pat, s2)
print(match_object) # <re.Match object; span=(1, 5), match='ytho'>

# \s matches whitespace character.
pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s2)
print(match_object) # <re.Match object; span=(3, 7), match='hon '>

s3 = """Hi there
We are learning Python
"""
pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s3)
print(match_object) # <re.Match object; span=(5, 9), match='ere\n'>

# \S is opposite of \s. It matches any character except, space \n and \t.
pat = r"[a-z][a-z][a-z]\S"
match_object = re.search(pat, s3)
print(match_object) # <re.Match object; span=(3, 7), match='ther'>

# \w - alphanumeric characters is [a-z], [A-Z], [0-9]
pat = r"[a-z][a-z][a-z]\w"
match_object = re.search(pat, s3)
print(match_object) # <re.Match object; span=(3, 7), match='ther'>

# \W - Opposite of \w - matches a character except [a-z],[A-Z],[0-9]
pat = r"[a-z][a-z][a-z]\W"
match_object = re.search(pat, s3)
print(match_object) # <re.Match object; span=(5, 9), match='ere\n'>