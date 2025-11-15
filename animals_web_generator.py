import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for fox in animals_data:
    name = fox["name"]
    diet = fox["characteristics"]["diet"]
    location = fox["locations"][0]
    type = fox["characteristics"].get("type")
    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {location}")
    if type:
        print(f"Type: {type}")
    print()