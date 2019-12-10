from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from db import OpStatus


class Todo(BaseModel):
    titulo: str
    status: Optional[OpStatus]


class TodoResponse(Todo):
    id: int
