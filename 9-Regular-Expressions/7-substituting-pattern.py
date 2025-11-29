import re
# sub() - substitute words.
s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = "Sunday"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result) # Friday, Monday, Tuesday, Monday, Friday

# Only replace one Sunday.
result = re.sub(pat, replacement, s1, count=1)
print(result) # Friday, Monday, Tuesday, Monday, Sunday

s1 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = r"S[a-z]+"
result = re.sub(pat, replacement, s1)
print(result) # Friday, Monday, Tuesday, Monday, Friday, Friday

message = """We are learning re. Using re, we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well."""

patt = r're'
replacement = "Regular Expressions"
result = re.sub(patt, replacement, message)
print(result)
# We aRegular Expressions learning Regular Expressions. Using Regular Expressions, we can search for a pattern in a given string.
# Using the sub(), we can Regular Expressionsplace the pattern with a given string as well.

patt = r'\bre\b'
replacement = "Regular Expressions"
result = re.sub(patt, replacement, message)
print(result)
# We are learning Regular Expressions. Using Regular Expressions, we can search for a pattern in a given string.
# Using the sub(), we can replace the pattern with a given string as well.

# If re is capital somewhere, that can also get replaced.
result = re.sub(patt, replacement, message, flags=re.IGNORECASE)
print(result)

phone_nums = "+91-1234567890, +91-999999999"
pattern = r"[+-]"
replacement = ""
result = re.sub(pattern, replacement, phone_nums)
print(result) # 911234567890, 91999999999