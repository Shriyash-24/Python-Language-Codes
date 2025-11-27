# os.path.exists()

import os
file_name = "C:/Users/Shri/Coding/TuteDude/Python Course/8-File-And-Exception-Handling/1-practice.txt"
if os.path.exists(file_name):
    print("File Exists")
else:
    print("File Doesn't Exist")

# You can use absolute path also, for windows replace back slash with forward slash.

# pathlib.Path.exists()

from pathlib import Path
file_name = Path("C:/Users/Shri/Coding/TuteDude/Python Course/8-File-And-Exception-Handling/1-practice.txt")
if file_name.exists():
    print("File Exists, Can't create.")
else:
    print("File Doesn't Exist, creating it.")
    fh = open(file_name, "xt")
    fh.write("Hello World")
    fh.close()


