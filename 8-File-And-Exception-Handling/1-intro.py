"""
Opening a file - open()
Takes file name as string and mode to open
open(file_name, mode_to_open)
Modes: r, x, w, a, t, b ( r - read, x - create, w - write, a - append, t - text file, b - binary mode )
"""

file_handler = open("1-practice.txt", 'rt') # rt is default mode.
print(file_handler) # <_io.TextIOWrapper name='1-practice.txt' mode='rt' encoding='cp1252'>

# When you open a file you need to close it too. It may lead to memory issues.
file_handler.close()
print(file_handler) # <_io.TextIOWrapper name='1-practice.txt' mode='rt' encoding='cp1252'>

# It still works but it doesn't mean that you should do it.