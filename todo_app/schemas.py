from pydantic import BaseModel
from datetime import datetime

class ToDoCreate(BaseModel):
    title :str
    description:str
    status:str
    
class ToDoResponse(ToDoCreate):
    task_id:int
    created_date=str    