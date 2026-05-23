from models import read_json,write_json
from datetime import datetime

def get_all_todos():
    return read_json()

def get_todo_id(task_id:int):
    todos=read_json()
    return next(())


current_time=datetime.now().strftime("%Y-%m-%d  %H:%M")

new_todo={
    "task_id":new_id,
    "task_name":task_name,
    "description":description,
    "status":status,
    "created_date":current_time
    
}
