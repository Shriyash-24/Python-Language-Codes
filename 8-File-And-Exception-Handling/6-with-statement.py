# Simplifies resource management by automatically handling setup and cleaning tasks.
# It ensures, resources are properly released. Makes the code clean.
# When working with files, it's important to open or close files.

# Without
fh = open("1-practice.txt","rt")
content = fh.read()
fh.close()
print(content) # Prints content of the file

with open("1-practice.txt","rt") as fh:
    contents = fh.read()
print(contents)

# Python makes sure that file is automatically closed.

with open("6-with-creation", "xt") as fh:
    fh.write("New File Creation Using with\n")
    fh.write("Good bye.")




