from fastapi import FastAPI
import uvicorn
from todo import todo_router


app = FastAPI(title="Todo List API")

@app.get("/")
async def welcome() -> dict:
    return{ "message": "Hello World !"}

app.include_router(todo_router)

