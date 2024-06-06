import strawberry

from src.model import AddTodoInput, Todo, list_todo


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_todo(self, todo: AddTodoInput) -> Todo:  # AddTodoInput for testing
        if todo.name in [t.name for t in list_todo]:
            return None
        list_todo.append(todo)
        return todo

    @strawberry.mutation
    def update_todo(self, name: str, done: bool) -> Todo:
        for todo in list_todo:
            if todo.name == name:
                todo.done = done
                return todo
        return None

    @strawberry.mutation
    def delete_todo(self, name: str) -> Todo:
        for i, todo in enumerate(list_todo):
            if todo.name == name:
                list_todo.pop(i)
                return todo
        return None
