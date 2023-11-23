import json
import csv
from pathlib import Path

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as json_input:
        data = json.load(json_input)

    if isinstance(data, list):
        keys = data[0].keys() if data else []
    elif isinstance(data, dict):
        keys = data.keys()
    else:
        raise ValueError("Invalid JSON format")

    connection = data["connections"]["connection"][0]
    fields = connection["field"]

    # Create a CSV file and write the tabular data
    with open("table.csv", mode="w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Field ID", "Encrypted Value Set", "Uses Encryption", "Component Override", "Use Default"])
    
        for field in fields:
            csv_writer.writerow([field["id"], field["encryptedValueSet"], field["usesEncryption"], field["componentOverride"], field["useDefault"]])

# Replace 'input.json' and 'output.csv' with your actual file names
json_file_path = Path(__file__).parent / 'test/test.json'
#json_file_path = '/test/test.json'
csv_file_path = 'output.csv'
json_to_csv(json_file_path, csv_file_path)

