from fastapi import APIRouter
from typing import List, Dict, Any, Optional
from models import Todo, TodoResponse
from db import TODO, OpStatus

todo_db = TODO()
router = APIRouter()


@router.get("/", response_model=List[TodoResponse])
def list_todos(status: Optional[OpStatus] = None):
    """
    View return all todos
    """
    if status is not None:
        return todo_db.filter(status=status)
    return todo_db.list()


@router.post("/", response_model=TodoResponse, status_code=201)
def insert_todo(todo_to_insert: Todo):
    """
    View insert item a new todo in list
    """
    return todo_db.insert(todo_to_insert.dict())


@router.get("/{id_todo}", response_model=TodoResponse)
def get_item_todo(id_todo: int):
    """
    View return a todo by id
    """
    return todo_db.get(id_todo)
