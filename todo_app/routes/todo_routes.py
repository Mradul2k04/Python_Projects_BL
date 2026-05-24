from fastapi import APIRouter , Path
from fastapi.responses import JSONResponse
from schemas import UpdateTask ,CreateTask
import crud

router = APIRouter()

# GET : Home page
@router.get('/')
def home():
    return {'message':'Task Manager(To-do list)'}

# GET : Fetch all tasks
@router.get('/tasks')
def view_tasks():
    return crud.get_all_tasks()

# GET : Fetch task by ID
@router.get('/tasks/{task_id}')
def task_by_id(task_id: str = Path(..., description='Task ID', example='T001')):
    return crud.get_tasks_by_id(task_id)   

# POST : Create new task
@router.post('/tasks')
def create_task(task: CreateTask):
    crud.add_task(task)
    return JSONResponse(status_code=201, content={'message':'Task created successfully'})

# PUT : Update task
@router.put('/edit_task/{task_id}')
def update_task(task_id: str, task_update: UpdateTask):
    crud.update_task(task_id,task_update)
    return JSONResponse(status_code=200, content={'message':'Task updated successfully'})

# DELETE : Delete task
@router.delete('/del_task/{id}')
def delete_extisting_todo(task_id: str):
    crud.delete_task(task_id)
    return JSONResponse(status_code=200, content={'message':'Task deleted successfully'})