from proto import todo_pb2


def listalltasks(stub):
    print("Listing all todos: ")
    all_todos = stub.ListAllTasks(todo_pb2.Empty())
    for task in all_todos.task:
        print(
            f"{task.id} {task.task_todo}, status: {task.status} (-1: not completed, 1: completed)"
        )
    all_todos = stub.ListAllStream(todo_pb2.Empty())
    for task in all_todos:
        print(
            f"{task.id} {task.task_todo}, status: {task.status} (-1: not completed, 1: completed)"
        )


def addtask(stub):
    content = input("Please enter the task todo: ")
    task = todo_pb2.Task(task_todo=content)
    response = stub.AddTask(task)
    # print(f"{response.task_todo} added succesfully")


def edittask(stub, option):
    edit_id = input("Please enter the id of the task to edit: ")
    task = todo_pb2.Task(id=int(edit_id))
    task = stub.GetTask(task)
    if option == "2":
        edit_content = input("Please enter the content of new task: ")
        task.task_todo = edit_content
    else:
        edit_status = input("1 for complete -1 for incomplete: ")
        task.status = int(edit_status)
    edit_task_response = stub.EditTask(task)
    # print(f"{edit_task_response.task_todo} updated succesfully")


def removetask(stub):
    del_id = input("Please enter the id of the task to delete: ")
    task = todo_pb2.Task(id=int(del_id))
    resp = stub.RemoveTask(task)
    print(f"{resp.id} removed succesfully")
