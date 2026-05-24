from fastapi import HTTPException
from database import load_data, save_data
from schemas import UpdateTask, CreateTask

# GET : Fetch all tasks
def get_all_tasks() -> dict:
    return load_data()

# GET : Fetch task by ID
def get_tasks_by_id(task_id: str) -> dict:
    data = load_data()
    if task_id not in data:
        raise HTTPException(status_code='404', detail='Task not found')
    
    return data[task_id]

# POST : Create new task
def add_task(task: CreateTask):
    data = load_data()
    if task.task_id in data:
        raise HTTPException(status_code=400, detail='Task already exists')
    
    data[task.task_id] = task.model_dump(exclude={'task_id'},mode = 'json')
    save_data(data)

# PUT : Update task
def update_task(task_id: str, task_upadte: UpdateTask):
    data = load_data()
    if task_id not in data:
        raise HTTPException(status_code=404, detail='Task not found')
    
    existing_task_info = data[task_id]
    updated_task_info = task_upadte.model_dump(exclude_unset=True,mode = 'json')

    for key, value in updated_task_info.items():
        existing_task_info[key] = value

    existing_task_info['task_id'] = task_id
    task_pydantic_obj = CreateTask(**existing_task_info)

    data[task_id] = task_pydantic_obj.model_dump(exclude={'task_id'},mode= 'json')
    save_data(data)

# DELETE : Delete task
def delete_task(task_id: str):
    data = load_data()
    if task_id not in data:
        raise HTTPException(status_code=404, detail='Task not found')
    
    del data[task_id]
    save_data(data)