# Regular Expressions - Special sequence of characters, that defines pattern for complex string matching functionalities.

message = "The current Python version is 3.14. Other previous versions are 3.12, 3.11, and so on."

# If Python is present in the message.
print("Python" in message) # True
print("14" in message) # True
print("09" in message) # False

# Where 14 is present, at which index and so on.
print(message.find('3.14')) # 30 is the index of 3.
print(message.find("Python")) # 12... first occurrence of Python.

# To use regular expressions, we use 're' module.
import re

# re.search() - Takes the RegEx pattern as first argument and string variable as 2nd argument.
match_obj = re.search("Python",message)
print(match_obj) # <re.Match object; span=(12, 18), match='Python'>
# If match is found, it returns a match object when there is a match found, else returns none.
# Span gives information about where the pattern is found and also displays what the match is.

if re.search("Python",message):
    print("Found") # In this we get "Found".
else:
    print("Not found")

print(message[12:18]) # Python


