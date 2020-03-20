from proto import todo_pb2
import grpc


def listalltasks(stub):
    try:
        all_todos = stub.ListAllTasks(todo_pb2.Empty())
        print("Listing all todos: ")
        for task in all_todos.task:
            print(
                f"{task.id} {task.task_todo}, status: {task.status} (-1: not completed, 1: completed)"
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
        for task in all_todos:
            print(
                f"{task.id} {task.task_todo}, status: {task.status} (-1: not completed, 1: completed)"
            )
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("Server is unavailable")
            raise e
        else:
            print(e.details())
            print(e.code())
            raise e


def addtask(stub):
    content = input("Please enter the task todo: ")
    task = todo_pb2.Task(task_todo=content)
    try:
        response = stub.AddTask(task)
    except grpc.RpcError as e:
        print(e.details())


def edittask(stub, option):
    edit_id = input("Please enter the id of the task to edit: ")
    task = todo_pb2.Task(id=int(edit_id))
    try:
        task = stub.GetTask(task)
        if option == "2":
            edit_content = input("Please enter the content of new task: ")
            task.task_todo = edit_content
        else:
            edit_status = input("1 for complete -1 for incomplete: ")
            task.status = int(edit_status)
        try:
            edit_task_response = stub.EditTask(task)
        except grpc.RpcError as e:
            print(e.details())
    except grpc.RpcError as e:
        print(e.details())


def removetask(stub):
    del_id = input("Please enter the id of the task to delete: ")
    task = todo_pb2.Task(id=int(del_id))
    try:
        resp = stub.RemoveTask(task)
        print(f"{resp.id} removed succesfully")
    except grpc.RpcError as e:
        print(e.details())
