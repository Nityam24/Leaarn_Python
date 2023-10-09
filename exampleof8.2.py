import json

# Step 1: Create a new JSON file with some data
new_data = {
    "new_key": "new_value",
    "another_key": [1, 2, 3],
    "nested_data": {
        "nested_key": "nested_value"
    }
}

new_file_name = "new_data.json"

with open(new_file_name, 'w') as new_json_file:
    json.dump(new_data, new_json_file, indent=4)
    
print(f"New JSON file '{new_file_name}' has been created.")

# Step 2: Copy the contents of an existing JSON file to another JSON file
source_file_name = "source.json"
destination_file_name = "destination.json"

with open(source_file_name, 'r') as source_file:
    source_data = json.load(source_file)

with open(destination_file_name, 'w') as dest_file:
    json.dump(source_data, dest_file, indent=4)

print(f"Contents of '{source_file_name}' have been copied to '{destination_file_name}'.")
