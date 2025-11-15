import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(fox):
    """Serialize a single animal dict into HTML card with name, diet, location and optional type."""
    output = ""
    name = fox["name"]
    diet = fox["characteristics"]["diet"]
    location = fox["locations"][0]
    type = fox["characteristics"].get("type")
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {diet}<br/>\n"
    output += f"<strong>Location:</strong> {location}<br/>\n"
    if type:
        output += f"<strong>Type:</strong> {type}<br/>\n"
    output += "\n"
    output += " </p>"
    output += '</li>'
    return output

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r") as file:
    html_page = file.read()

output = ""
for fox in animals_data:
    output += serialize_animal(fox)


new_html = html_page.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)