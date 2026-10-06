import json
import openpyxl

# Open the Excel file
input_file = "Assig9input.xlsx"

workbook = openpyxl.load_workbook(input_file, data_only=True)
sheet = workbook.active

# Get column headings from the first row
headers = [cell.value for cell in sheet[1]]

# Convert Excel data into a list of dictionaries
data = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    record = {}

    for header, value in zip(headers, row):
        record[header] = value

    data.append(record)

# Write the data into a JSON file
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, default=str)

print("Excel data successfully converted to JSON.")
print("Output stored in output.json")