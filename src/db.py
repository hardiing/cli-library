import json
import os

FILENAME = "library_db.json"

def add_to_db(book):
    json_obj = json.dumps(book)
    
    if os.path.exists(FILENAME) and os.stat(FILENAME).st_size != 0:
        with open(FILENAME, "r") as file:
            file_data = json.load(file)
    else:
        file_data = []
    
    if isinstance(file_data, list):
        file_data.append(json_obj)
    else:
        print("Error: JSON file does not contain a list.")

    with open(FILENAME, "w") as file:
        json.dump(file_data, file, indent=4)