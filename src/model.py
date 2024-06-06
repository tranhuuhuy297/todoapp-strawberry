import strawberry


@strawberry.type
class Todo:
    name: str
    done: bool


list_todo = [
    Todo(name="Todo #1", done=False),
    Todo(name="Todo #2", done=False),
    Todo(name="Todo #3", done=True)
]
