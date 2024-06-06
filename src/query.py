from typing import List

import strawberry

from src.model import Todo, list_todo


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"

    @strawberry.field
    def list_todo(self, info, done: bool = None) -> List[Todo]:
        if done is None:
            return list_todo
        return filter(lambda todo: todo.done == done, list_todo)
