fh = open("1-practice.txt", "rt")
contents = fh.read()
fh.close()

print(contents) # Will print the content of the file.

# If I type file_name incorrectly and then trying to read, then file not found error will come.
# If we open in read more and trying to write it, then also ERROR.
# If I open file in append more, or write mode and try to read it.. then ERROR.
# If I open in write mode, but then with 1st line.. file content gets deleted. Then try to read it and ERROR will come.
# If I use create mode, you can't read the file.
# If I try to create on existing file, then also ERROR.