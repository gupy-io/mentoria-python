from typing import List, Dict, Any, Optional, Union
from enum import Enum


class OpStatus(str, Enum):
    todo = "TODO"
    in_progress = "WIP"
    done = "DONE"


todozinho = Dict[str, Union[int, str, OpStatus]]


class TODO:
    todo: List[todozinho] = [
        {
            "id": 1,
            "titulo": "Fazer almoco",
            "decricao": "Tem que fazer almoco",
            "status": OpStatus.todo,
        },
        {
            "id": 2,
            "titulo": "Jogar um dotinha",
            "status": OpStatus.todo,
        },
        {
            "id": 3,
            "titulo": "Correr",
            "status": OpStatus.todo,
        },
    ]
    id_atual = 3

    def list(self):
        return self.todo

    def insert(self, item: todozinho) -> todozinho:
        self.id_atual += 1
        item[id] = self.id_atual
        self.todo.append(item)
        return item

    def get(self, item_id: int) -> todozinho:
        item = filter(lambda x: x["id"] == item_id, self.todo)
        return list(item)[0]

    def filter(self, status: OpStatus) -> List[todozinho]:
        return list(filter(lambda x: x["status"] == status, self.todo))
