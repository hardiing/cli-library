import json
import os

FILENAME = "library_db.json"
WISHLIST = "wishlist_db.json"

def add_to_db(book):
    json_obj = json.dumps(book)
    json_obj = flatten_json(json_obj)
    
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

def flatten_json(y):
    out = {}

    def flatten(x, name=""):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + "_")
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(a, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = x
    
    flatten(y)
    return out

def add_to_wishlist(book):
    json_obj = json.dumps(book)
    json_obj = flatten_json(json_obj)
    
    if os.path.exists(WISHLIST) and os.stat(WISHLIST).st_size != 0:
        with open(WISHLIST, "r") as file:
            file_data = json.load(file)
    else:
        file_data = []
    
    if isinstance(file_data, list):
        file_data.append(json_obj)
    else:
        print("Error: JSON file does not contain a list.")

    with open(WISHLIST, "w") as file:
        json.dump(file_data, file, indent=4)

def search_library(book):
    json_obj = json.dumps(book)
    json_obj = flatten_json(json_obj)

    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
        
        if json_obj in data:
            print("---Book exists in library---")
        else:
            print("---No matches found in library---")
    except FileNotFoundError:
        print("Library file not found.")
        exit()

def search_wishlist(book):
    json_obj = json.dumps(book)
    json_obj = flatten_json(json_obj)

    try:
        with open(WISHLIST, "r") as file:
            data = json.load(file)
        
        if json_obj in data:
            print("---Book exists in wishlist---")
        else:
            print("---No matches found in wishlist---")
    except FileNotFoundError:
        print("Wishlist file not found.")
        exit()

