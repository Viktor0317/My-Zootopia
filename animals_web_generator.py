
import json


def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

animals_data = load_data("animals_data.json")

for animal in animals_data:
    animal_name = animal["name"]
    animal_diet = animal["characteristics"]["diet"]
    animal_location = animal["locations"][0]
    animal_type = animal["characteristics"].get("type", "Unknown")
    print(
        f"Name: {animal_name}\n"
        f"Diet: {animal_diet}\n"
        f"Location: {animal_location}\n"
        f"Type: {animal_type}\n"
    )
