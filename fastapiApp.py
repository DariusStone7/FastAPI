from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from todo import todo_router

app = FastAPI(title="Todo List API")

# Configuration du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Ajoutez l'URL de votre application Vue.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def welcome() -> dict:
    return{ "message": "Hello World !"}

app.include_router(todo_router)

