from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    created_at: str
    expire_at: str
    updated_at: str

