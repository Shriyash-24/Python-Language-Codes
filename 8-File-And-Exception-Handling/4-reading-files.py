# We have a function called - read()
# Reads contents of a file as str.

file_handler = open('3-w-mode.txt', 'rt')
content = file_handler.read()

print(content) # This file is overwritten using 'w' mode in Python
print(type(content)) # <class 'str'>

file_handler.seek(0) # Move pointer back to start.

content = file_handler.read(10)
print(content) # reads first 10 characters - This file

file_handler.seek(0) # Move pointer back to start.

# readline()
result = file_handler.readline()
print(result) # This file is overwritten using 'w' mode in Python


# readlines()
file_handler.seek(0)
lines = file_handler.readlines()
print(lines) # ["This file is overwritten using 'w' mode in Python"]
print(type(lines)) # <class 'list'>

# Each line (including \n) as a element of a list will be stored.
# readline() reads only one line, readlines() add all lines (including \n) will be stored in list.

# We can print lines using for loop.
for line in lines:
    print(line) # Also prints \n.
    print(line.rstrip('\n')) # Removes \n :)