input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

with open(output_file, "w") as file:
    file.writelines(lines[:2])

print("First two lines written to", output_file)