import pandas as pd
import json
from pathlib import Path
import csv

# Specify the path to your JSON file
json_file_path = Path(__file__).parent / 'test/test.json'


# Read JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Extract required columns
data = []
for item in json_data:
    if "connection" in item:
        for connection_item in item["connection"]:
            data.append(
                {
                    "component name": item["name"],
                    "field": connection_item["id"],
                    "component type": item["component_type"],
                    "value": connection_item["value"],
                }
            )
    elif "processProperty" in item:
        for property_item in item["processProperty"]:
            data.append(
                {
                    "component name": item["name"],
                    "field": property_item["id"],
                    "component type": item["component_type"],
                    "value": property_item["value"],
                }
            )
    elif "crossReference" in item:
        for reference_item in item["crossReference"]:
            data.append(
                {
                    "component name": item["name"],
                    "field": reference_item["id"],
                    "component type": item["component_type"],
                    "value": reference_item["value"],
                }
            )
    elif "dynamicProcessProperty" in item:
        for dynamic_property_item in item["dynamicProcessProperty"]:
            data.append(
                {
                    "component name": "dynamicProcessProperty",
                    "field": dynamic_property_item["id"],
                    "component type": item["component_type"],
                    "value": dynamic_property_item["value"],
                }
            )

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_csv("out.csv", index=False)
