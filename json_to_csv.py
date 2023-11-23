import csv
import json

def json_to_table(json_data, parent_key='', table=None):
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
    
    return table

# Your JSON data
json_data = {
    "@type": "EnvironmentExtensions",
    "connections": {
        "@type": "Connections",
        "connection": [
            {
                "@type": "Connection",
                "field": [
                    {
                        "@type": "Field",
                        "id": "authType",
                        "encryptedValueSet": False,
                        "usesEncryption": False,
                        "componentOverride": False,
                        "useDefault": True
                    },
                    # ... (other fields)
                ],
                "id": "4d3f80eb-5a5e-421e-b596-c5a56e739607",
                "name": "Boomi_Service_Slack_Connector"
            }
        ]
    },
    "operations": {
        "@type": "Operations",
        "operation": [
            # ... (other operations)
        ]
    },
    "environmentId": "b8ece4bb-0306-45dc-8911-c31dd6e11d14",
    "extensionGroupId": "",
    "id": "b8ece4bb-0306-45dc-8911-c31dd6e11d14"
}

# Convert JSON to nested table structure
table_structure = json_to_table(json_data)

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

