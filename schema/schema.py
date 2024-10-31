import json
import os
import sys

def split_schema(schema, base_path, definitions_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    process_schema(schema, base_path, definitions_path, output_dir)
    main_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": schema.get("title", "MainSchema"),
        "$id": f"{base_path}/{schema.get('title','main')}.json",
        "type": schema.get("type", "object"),
        "properties": schema.get("properties"),
        "required": schema.get("required")
    }
    with open(os.path.join(output_dir, f"{schema.get('title','main')}.json"), 'w') as f:
        json.dump(main_schema, f, indent=2)

def process_schema(schema_part, base_path, definitions_path, output_dir):
    if isinstance(schema_part, dict):
        # If 'type' is 'object' and 'properties' exists, consider splitting
        if schema_part.get("type") == "object" and "properties" in schema_part:
            for prop_name, prop_value in schema_part["properties"].items():
                if isinstance(prop_value, dict):
                    # If the property is a complex type, extract it
                    title = prop_value.get("title", prop_name)
                    prop_id = f"{base_path}/{definitions_path}/{title}.json"
                    prop_value["$id"] = prop_id
                    # Write the property schema to a file
                    prop_file_path = os.path.join(output_dir, definitions_path, f"{title}.json")
                    os.makedirs(os.path.dirname(prop_file_path), exist_ok=True)
                    with open(prop_file_path, 'w') as f:
                        json.dump(prop_value, f, indent=2)
                    # Replace the property with a $ref
                    schema_part["properties"][prop_name] = {"$ref": prop_id}
                else:
                    process_schema(prop_value, base_path, definitions_path, output_dir)
        else:
            for key, value in schema_part.items():
                process_schema(value, base_path, definitions_path, output_dir)
    elif isinstance(schema_part, list):
        for item in schema_part:
            process_schema(item, base_path, definitions_path, output_dir)

if __name__ == "__main__":
    # Replace with your actual file paths and base path
    input_schema_file = 'input_schema.json'  # The original schema file
    base_path = 'http://example.com/schemas'  # The base path for $id
    definitions_path = 'definitions'  # The subdirectory for definitions
    output_dir = 'output_schemas'  # The directory to write the output schemas

    with open(input_schema_file, 'r') as f:
        schema = json.load(f)
    split_schema(schema, base_path, definitions_path, output_dir)