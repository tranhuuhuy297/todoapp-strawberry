import strawberry

from src.model import Todo


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_todo(self, name: str, done: bool) -> Todo:
        return Todo(name=name, done=done)
