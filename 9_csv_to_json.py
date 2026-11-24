# Read data from a CSV file and convert it to JSON
import csv
import json

input_file = "input.csv"
output_file = "output.json"

try:
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        data = list(csv.DictReader(csv_file))

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV data successfully converted to {output_file}")
except FileNotFoundError:
    print(f"Error: {input_file} was not found.")
