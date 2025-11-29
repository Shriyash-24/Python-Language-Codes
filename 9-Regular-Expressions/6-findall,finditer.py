# match() - Looks for the pattern at the beginning of the string.
import re

s1 = "We are learning regex in Python"
pat = r"[A-Z][a-z]"
match_obj = re.match(pat,s1)
print(match_obj) # <re.Match object; span=(0, 2), match='We'>

pat = r"[a-z]{3}"
match_obj = re.match(pat,s1)
print(match_obj) # None, basically at the beginning of s1, there were not 3 consecutive lowercase letters.

phones = "John-1234567890, Carol-9876543210, Mark-9087654321, ALice-3434340"
pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj) # <re.Match object; span=(5, 15), match='1234567890'>

# Findall gives us all the matches in a list.
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321']

# What if I want all the phone numbers..
pat = r"[0-9]+" # We wanted 1 or more digits..
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321', '3434340']

phones = "John-1234567890, Carol-9876543210, Mark-9087654321, ALice-3434340, Python3.13.5"
pat = r"[0-9]+" # We wanted 1 or more digits..
match_obj = re.findall(pat, phones)
print(match_obj)

# Fetch all phone numbers, the phone numbers are exactly 7 digits and should not exceed 15 digits.
pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321', '3434340']

# Fetch all phone numbers, the phone number are atleast 7 digits.
pat = r"[0-9]{7,}"
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321', '3434340']

phones = "John-1234567890, Carol-9876543210, Mark-9087654321, ALice-3434340, Python3.13.5, Dan-123456789987654323456"
pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321', '3434340', '123456789987654']

# In upper case it gives me Dan's phone number but only till 15 digits.. what if I don't want it.
pat = r"\b[0-9]{7,15}\b" # \b - boundary.. we can use it for start and end as well.
match_obj = re.findall(pat, phones)
print(match_obj) # ['1234567890', '9876543210', '9087654321', '3434340']

# finditer() - Iterator of all match objects.
pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phones)
print(match_obj_iter) # <callable_iterator object at 0x0000021CF3146680>

# To see all match objects..
for matches in match_obj_iter:
    print(matches)
# O/P -
# <re.Match object; span=(5, 15), match='1234567890'>
# <re.Match object; span=(23, 33), match='9876543210'>
# <re.Match object; span=(40, 50), match='9087654321'>
# <re.Match object; span=(58, 65), match='3434340'>










