import json

DATA_FILE = "data.json"

def load_items():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_items(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=4)