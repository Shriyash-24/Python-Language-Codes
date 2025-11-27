# x mode => create a file

fh = open("2-file1.txt", 'xt')

# Writing into a file
fh.write("This file is created using the 'x' mode in Python. \n")
fh.write("Next line")

# Close the file
fh.close()

# You can't create an already existing using the x mode.

#fh.write("test") # After closing the file, you can't do write operation. ERROR.

