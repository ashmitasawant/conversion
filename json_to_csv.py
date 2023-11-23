import csv
import json
from pathlib import Path
def json_to_table(json_data, parent_key='', table=None):
    with open(json_data, 'r') as json_input:
        data = json.load(json_input)
        
    if table is None:
        table = {}
    
    if isinstance(json_data, dict):
        for k, v in json_data.items():
            new_key = f"{parent_key}/{k}" if parent_key else k
            json_to_table(v, new_key, table)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            new_key = f"{parent_key}/{i}" if parent_key else str(i)
            json_to_table(item, new_key, table)
    else:
        table[parent_key] = json_data
    
   





# Convert JSON to nested table structure
table_structure = json_to_table(data)

# Print the result
for key, value in table_structure.items():
    print(f"{key}: {value}")

csv_file_path = 'output.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Key', 'Value'])

    for key, value in table_structure.items():
        csv_writer.writerow([key, value])

print(f"CSV file '{csv_file_path}' created successfully.")
# Replace 'input.json' and 'output.csv' with your actual file names
json_file_path = Path(__file__).parent / 'test/test.json'
#json_file_path = '/test/test.json'
csv_file_path = 'output.csv'

json_to_table(json_file_path, csv_file_path)
