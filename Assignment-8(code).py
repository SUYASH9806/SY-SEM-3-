with open("input.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

with open("output.txt", "w") as file:
    file.writelines(lines[:2])

print("First two lines have been written to output.txt")