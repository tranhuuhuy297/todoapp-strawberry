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


@strawberry.input
class AddTodoInput:
    name: str = strawberry.field(description="The name of todo")
    done: bool = strawberry.field(description="The status of todo")
