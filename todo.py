from fastapi import APIRouter, HTTPException, Form
from model import Todo
from typing import Optional #to add an parametter optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

todo_router = APIRouter()
todo_list = []

#function to add an todo in todo list
# @todo_router.post("/todo", response_model=TodoOut, response_model_exclude={'password'})
@todo_router.post("/todo")
async def add_todo(todo:Todo) -> dict:
    todo_list.append(todo)
    return {"todo":todo}

#function to get all todos
@todo_router.get("/todo")
async def retrive_todos() -> dict:
    return {"todos":todo_list}

#function to get an todo in todo list
@todo_router.get("/todo/{id}")
async def retrive_single_todo(id: int):
    try:
        if (0 <= id < len(todo_list)):
            return todo_list[id]
    except:
        raise HTTPException(status_code=404, detail="todo not found")


#function to update an todo in todo list
@todo_router.put("/todo/{id}")
async def update_todo(id: int, todo:Todo):
    try:
        if (0 <= id < len(todo_list)):
            todo_list[id] = todo

        return todo_list[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")
    
#function to delete an todo in todo list
@todo_router.delete("/todo/{id}")
async def delete_todo(id:int):
    try:
        if (0 <= id < len(todo_list)):
            todo = todo_list[id]
            del todo_list[id]
        return todo
    except:
        raise HTTPException(status_code=404, detail="todo not found")
    