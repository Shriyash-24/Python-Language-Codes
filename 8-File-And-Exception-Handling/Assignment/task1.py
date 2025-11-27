"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

try:
    with open("task1.txt", "r") as fh: # Used with to handle file closing operations automatically
        print("Reading file content..")
        no_of_lines = 0 # Used to depict the number of lines.

        while True: # Used a loop so all the lines in a file, may be read.
            line = fh.readline() # Using readline(), a single line of the file is stored in line.
            if line == "": # Checks if line is empty, basically the end of file.
                break # Condition to get out of loop.
            no_of_lines += 1 # Increasing line number, earlier 0.
            print(f"Line {no_of_lines} - {line}")
except FileNotFoundError: # Addresses the exception of file not found.
    print("Error: The file 'task1.txt' was not found.")

