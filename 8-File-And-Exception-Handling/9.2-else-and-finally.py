

# with open("my_file.txt", "rt") as fh:
#     data = fh.read()
# print(data)

# Error - Can't read a file that doesn't exist.

try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()
    print(data)
except FileNotFoundError:
    print("File not found.")

# We want to know the error message.
try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()
    print(data)
except FileNotFoundError as file_err:
    print("File not found.")
    print(file_err) # [Errno 2] No such file or directory: 'my_file.txt'

# else block - Fallback option. If no error happens in try block, you want to do that activity in else block.
# Generally used to do verification steps, where we don't want certain errors to hide.

try:
    with open("ninepointtwo.txt", "rt") as fh:
        data = fh.read()
except FileNotFoundError as file_err:
    print("File not found.")
    print(file_err)
else:
    print(data) # Since no exceptions happened, it comes to else block.

# else is exceuted when there is no exception.
# Now, apart try-except-else we also have finally keyword.
import io
try:
    fh = open("file10000.txt", "wt") # if issue happens here then it will look for exceptions
    data = fh.read() # it will fail.. will give unsupported operation..
except FileNotFoundError as file_err:
    print("File not found.")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err) # prints this
else: # will not get executed because exception happened
    print(data)
finally:
    print("Finally block") # this executes..
    # File closing is not done.
    fh.close() # this has to be done.. if there is no error or error.

# try and except should be there, else and finally may or may not be there.





