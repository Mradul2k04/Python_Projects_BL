from datetime import datetime
from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field


class CreateTask(BaseModel):
    task_id : Annotated[str,Field(..., description='Task ID',examples=['T001','T002'])]
    task_name : Annotated[str,Field(..., description='Task Name')]
    description : Annotated[str , Field(description= 'Describe the  Task',default=None)]
    status : Annotated[Literal["Completed", "Pending","other"], Field(description='Status of Task' ,default= "Pending")]
    created_at : Annotated[Optional[datetime] , Field(default_factory=lambda: datetime.now(),description='Task creation timestamp (UTC)')]
    updated_at : Annotated[Optional[datetime] ,Field(default= None, description='Task updation timestamp (UTC)')]

class UpdateTask(BaseModel):
    task_name : Annotated[Optional[str],Field(default=None, description='Task Name')]
    description : Annotated[Optional[str] , Field(default=None,description= 'Describe the Task', max_length=180, min_length=10)]
    status : Annotated[Optional[Literal["Completed", "Pending","other"]], Field(description='Status of Task' ,default= "Pending")]
    updated_at : Annotated[Optional[datetime] , Field(default= lambda: datetime.now(), description='Task updation timestamp (UTC)')]