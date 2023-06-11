from pydantic import BaseModel

class Item (BaseModel):
    item : str
    status : str


class TodoOut (BaseModel):
    id : int
    item : Item


class TodoIn(BaseModel):
    password: str
    id : int
    item : Item

