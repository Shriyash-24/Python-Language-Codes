"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

# Step 1 - Write (Overwrite the file).
with open('task2.txt', 'w') as fh:
    user_input = input("Enter text to write to the file: ")
    fh.write(user_input + "\n") # \n is used to write file content neatly.
    print("Data successfully written to task2.txt.")

# Step 2 - Append.
with open('task2.txt', 'a') as fh:
    user_additional = input("Enter additional text to append: ")
    fh.write(user_additional + "\n") # \n is used to write file content neatly.
    print("Data successfully appended.")

# Step 3 - Read final content.
with open('task2.txt', 'r') as fh:
    print("Final content of task2.txt: ")
    for line in fh: # Loop to read the file content.
        print(line)


