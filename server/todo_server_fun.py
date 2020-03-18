from proto import todo_pb2


tasks = {}
counter = 1


def listalltasks():
    all_tasks = todo_pb2.AllTasks()
    for task_id in sorted(tasks):
        all_tasks.task.append(tasks[task_id])
    return all_tasks


def listallstream():
    all_tasks = []
    for task_id in sorted(tasks):
        task = todo_pb2.Task(
            id=tasks[task_id].id,
            task_todo=tasks[task_id].task_todo,
            status=tasks[task_id].status,
        )
        all_tasks.append(task)
    return all_tasks


def gettask(request):
    task = tasks[request.id]
    return task


def addtask(request):
    global counter
    new_task = todo_pb2.Task(id=counter, task_todo=request.task_todo, status=-1)
    tasks[counter] = new_task
    counter = counter + 1
    return new_task


def edittask(request):
    tasks[request.id] = request
    return tasks[request.id]


def deletetask(request):
    del tasks[request.id]
