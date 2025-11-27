# 'a' mode ==> Append mode

fh = open("1-practice.txt", 'at') # append text file

fh.write("\n\nThis content has been written by 5-appending.py\n")
fh.write("'a' mode is used to add new content at the end of the file.\n")
fh.write("Good bye!")

fh.close()

# If the file doesn't exist, 'a' mode creates the file.

fh = open("5-append.txt", 'at')
fh.write("\nThis content has been written by 5-appending.py\n")
fh.write("'a' mode is used to add new content at the end of the file.\n")
fh.write("Good bye!")
