# Count lines, extract the first two lines, and write them to a new file

input_file = "input.txt"
output_file = "extracted.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("Total number of lines:", len(lines))
    first_two_lines = lines[:2]

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(first_two_lines)

    print("First two lines written to", output_file)
except FileNotFoundError:
    print(f"Error: {input_file} was not found.")
