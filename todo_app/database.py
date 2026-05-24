import json
import os

file_path = 'task.json'

def load_data() -> dict:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(data: dict):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
        
        
load_data()