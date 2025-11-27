# w mode - Open the file for writing. Overwrites the file.

fh = open('2-file1.txt', 'wt') # File content got deleted

fh.write("This file is overwritten using 'w' mode in Python")
fh.close()

# Changes can't be reverted. Be very careful.

fh = open('3-w-mode.txt', 'wt') # File didn't exist then we created it.
fh.write("This file is overwritten using 'w' mode in Python")