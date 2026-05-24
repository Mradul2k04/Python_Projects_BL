from fastapi import FastAPI
from routes.todo_routes import router as todo_router


app=FastAPI(
    title="To-Do API"
)

app.include_router(todo_router,prefix='/todo',tags={"Curd Router"})