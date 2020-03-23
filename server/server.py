# from proto import todo_pb2
from proto import todo_pb2_grpc
from .helpers import list_all_todos, list_all_stream, get_todo, add_todo, edit_todo, remove_todo


class TodoAppServicer(todo_pb2_grpc.TodoAppServicer):
    def ListAllTodos(self, request, context):
        all_todos = list_all_todos()
        return all_todos

    def ListAllStream(self, request, context):
        all_todos = list_all_stream()
        for todo in all_todos:
            yield todo

    def GetTodo(self, request, context):
        todo = get_todo(request, context)
        return todo

    def AddTodo(self, request, context):
        new_todo = add_todo(request, context)
        return new_todo

    def EditTodo(self, request, context):
        edited_todo = edit_todo(request, context)
        return edited_todo

    def RemoveTodo(self, request, context):
        remove_todo(request, context)
        return request
