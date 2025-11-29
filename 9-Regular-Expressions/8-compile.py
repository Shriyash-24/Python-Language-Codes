import re

phones = "Alice-1234567890, Mark-0987654321, Carol-1357908642"
pattern = r"\d{10}"
match_obj = re.findall(pattern, phones)
print(match_obj) # ['1234567890', '0987654321', '1357908642']

pattern_compiled = re.compile(pattern)
print(pattern_compiled) # re.compile('\\d{10}')
print(type(pattern_compiled)) # <class 're.Pattern'>
match_obj = re.findall(pattern_compiled, phones)
print(match_obj) # ['1234567890', '0987654321', '1357908642']

# Why do we need compile, it produces same output ~ It optimizes the time.

with open("student_details", "rt") as fh:
    data = fh.read()

print(data) # We get data as string.
phones_matches = re.finditer(pattern_compiled, data)
print(phones_matches) # <callable_iterator object at 0x000001F3E9945F60>

for matches in phones_matches:
    print(matches) # O/P - <re.Match object; span=(24, 34), match='9876543210'>
                        #  <re.Match object; span=(59, 69), match='1234567890'>
                        #  <re.Match object; span=(92, 102), match='0987654321'>
