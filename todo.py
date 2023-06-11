from fastapi import APIRouter, HTTPException, Form
from model import TodoIn, TodoOut
from typing import Optional #to add an parametter optional

todo_router = APIRouter()
todo_list = []

#function to add an todo in todo list
@todo_router.post("/todo", response_model=TodoOut, response_model_exclude={'password'})
async def add_todo(todo:TodoIn) -> dict:
    todo_list.append(todo)
    return todo

#function to get all todos
@todo_router.get("/todo")
async def retrive_todos() -> dict:
    return {"todos":todo_list}

#function to get an todo in todo list
@todo_router.get("/todo/{id}")
async def retrive_single_todo(id: int):
    try:
        for i in range(len(todo_list)):
            if (todo_list[i].id == id):
                return todo_list[i]
    except:
        raise HTTPException(status_code=404, detail="todo not found")


#function to update an todo in todo list
@todo_router.put("/todo/{id}")
async def update_todo(id: int, todo:TodoIn):
    try:
        j = None
        for i in range(len(todo_list)):
            if (todo_list[i].id == id):
                todo_list[i] = todo
                j = i
                break

        return todo_list[j]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")
    
#function to delete an todo in todo list
@todo_router.delete("/todo/{id}")
async def delete_todo(id:int):
    try:
        for i in range(len(todo_list)):
            if (todo_list[i].id == id):
                todo = todo_list[i]
                del todo_list[i]
        return todo
    except:
        raise HTTPException(status_code=404, detail="todo not found")
    