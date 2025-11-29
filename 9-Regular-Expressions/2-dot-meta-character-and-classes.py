# Character classes - [] - Anything inside [] means: Match any character from this set.
"""
[0-9] → match any single digit
[a-z] → match any lowercase letter
[A-Z] → match any uppercase letter
"""

import re
message = "The current Python version is 3.14. Other previous versions are 3.12, 3.11, and so on."

match_object = re.search("[0-9][0-9]", message) # Here we are trying to match two consecutive digits.
print(match_object) # <re.Match object; span=(32, 34), match='14'>

# The search function was trying to match the first occurrence of the match.
# You can write like this as well..

match_object = re.search("[0123456789][0-9]", message)
print(match_object) # <re.Match object; span=(32, 34), match='14'>

match_object = re.search("[0-9][0-9]", "House number: 251/A")
print(match_object) # <re.Match object; span=(14, 16), match='25'>

match_object = re.search("[0-9][0-9][0-9]", "House number: 251/A")
print(match_object) # <re.Match object; span=(14, 17), match='251'>

# Another meta character is . - Match any single character except newline.
match_object = re.search("[0-9].[0-9][0-9]", message)
# [0-9].[0-9][0-9] - It means - Digit, Any Character, Digit, Digit.
# 3.14 matches the string perfectly.
print(match_object) # <re.Match object; span=(30, 34), match='3.14'>

# In the above example, [0-9].[0-9] - digit, any character, digit.
match_object = re.search("[0-9].[0-9]", "House number: 251/A")
print(match_object) # <re.Match object; span=(14, 17), match='251'>
# Here '5' is the any character.

# . - It means any character, except new line character.

message_1 = "The year is 2011"
match_object = re.search("[0-9].[0-9][0-9]", message_1)
print(match_object) # <re.Match object; span=(12, 16), match='2011'>

# [.] means match the literal dot character - .
message_1 = "The year is 2011"
match_object = re.search("[0-9][.][0-9][0-9]", message_1)
print(match_object) # None

match_object = re.search("[0-9][.][0-9][0-9]", message)
print(match_object) # <re.Match object; span=(30, 34), match='3.14'>



