from proto import todo_pb2
import grpc


def list_all_todos(stub):
    """
    Lists all the todos in the database by calling the server side function and printing them to
    the console.

    Args:
        stub: a grpc stub

    Returns:
        None

    Raises:
        grpc.RpcError:
            If server is unavailable
    """
    try:
        all_todos = stub.ListAllTodos(todo_pb2.Empty())
        print("Listing all todos: ")
        for todo in all_todos.todo:
            print(
                f"{todo.id} {todo.content}, status: {todo.status} (0: not completed, 1: completed)"
            )
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("Server is unavailable")
            raise e
        else:
            print(e.details())
            print(e.code())
            raise e
    try:
        all_todos = stub.ListAllStream(todo_pb2.Empty())
        for todo in all_todos:
            print(
                f"{todo.id} {todo.content}, status: {todo.status} (0: not completed, 1: completed)"
            )
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("Server is unavailable")
            raise e
        else:
            print(e.details())
            print(e.code())
            raise e


def add_todo(stub):
    """
    Add a todo to the database

    Args:
        stub: a grpc stub

    Returns:
        todo_pb2.Todo object

    Raises:
        grpc.RpcError: If content is more than 200 characters
    """
    content = input("Please enter the task todo: ")
    todo = todo_pb2.Todo(content=content)
    try:
        response = stub.AddTodo(todo)
        print(response)
    except grpc.RpcError as e:
        print(e.details())


def edit_todo(stub, option):
    """
    Edits an existing todo

    Args:
        stub: grpc stub
        option(str): Option to choose between editing content and status

    Returns:
        todo_pb2.Todo object

    Raises:
        grpc.RpcError:
            If content is more than 200 characters
            If id entered is not present in database
    """
    edit_id = input("Please enter the id of the todo to edit: ")
    todo = todo_pb2.Todo(id=int(edit_id))
    try:
        todo = stub.GetTodo(todo)
        if option == "2":
            edit_content = input("Please enter the new content for todo: ")
            todo.content = edit_content
        else:
            edit_status = input("1 for complete 0 for incomplete: ")
            todo.status = int(edit_status)
        try:
            edit_todo_response = stub.EditTodo(todo)
            print(edit_todo_response)
        except grpc.RpcError as e:
            print(e.details())
    except grpc.RpcError as e:
        print(e.details())


def remove_todo(stub):
    """
    Removes an existing todo

    Args:
        stub: grpc stub
        option(str): Option to choose between editing content and status

    Returns:
        todo_pb2.Todo object

    Raises:
        grpc.RpcError: If id entered is not present in database
    """
    del_id = input("Please enter the id of the task to delete: ")
    todo = todo_pb2.Todo(id=int(del_id))
    try:
        resp = stub.RemoveTodo(todo)
        print(f"{resp.id} removed succesfully")
    except grpc.RpcError as e:
        print(e.details())
