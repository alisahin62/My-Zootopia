import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r") as file:
    html_page = file.read()

output = ""
for fox in animals_data:
    name = fox["name"]
    diet = fox["characteristics"]["diet"]
    location = fox["locations"][0]
    type = fox["characteristics"].get("type")
    output += '<li class="cards__item">'
    output += f"Name: {name}<br/>\n"
    output += f"Diet: {diet}<br/>\n"
    output += f"Location: {location}<br/>\n"
    if type:
        output += f"Type: {type}<br/>\n"
    output += "\n"
    output += '</li>'

new_html = html_page.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)