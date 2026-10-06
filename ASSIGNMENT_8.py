# Program to read a file, count lines, and extract first two lines

with open("ASSIGNMENT_8_INPUT_.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)

print("Total number of lines:", line_count)

first_two_lines = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines have been written to output.txt")