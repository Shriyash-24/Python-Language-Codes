# ^ - Caret
import re
# We want to match language.
s1 = "Python is a programming language"
pat = r"[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj) # <re.Match object; span=(12, 20), match='programm'>

# Caret symbol checks at the beginning.. do we have eight symbols starting from lowercase? No.
pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj) # None

# $ - matches the end of the string ~ Will check end of string.
pat = r"[a-z]{8}$"
match_obj = re.search(pat, s1)
print(match_obj) # <re.Match object; span=(24, 32), match='language'>

# group - () and | (or)
emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com|edu)"
match_obj = re.search(pat, emails)
print(match_obj) # <re.Match object; span=(16, 19), match='com'>
# Match the first instance, and we either of com or edu. So we get com.

# Round brackets match exactly.
emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com)"
match_obj = re.search(pat, emails)
print(match_obj) # <re.Match object; span=(16, 19), match='com'>

# Square brackets match one of the elements in the [].
emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"[com]"
match_obj = re.search(pat, emails)
print(match_obj) # <re.Match object; span=(2, 3), match='c'>



