import json
import os

File_Path="todo_app/Data.json"

def read_json():
    if not os.path.exists(File_Path):
        return []
    with open(File_Path,"r") as f:
        return json.load(f)
    
def write_json(data:list):
    with open(File_Path,"w") as f:
        json.dump(data,f,indent=4)  
        
              
        