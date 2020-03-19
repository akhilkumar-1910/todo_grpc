from proto import todo_pb2
from sqlalchemy import create_engine
from models.todo_sqlalchemy import Task
from sqlalchemy.orm import sessionmaker
import os


dbuser = os.environ.get("dbuser")
dbpassword = os.environ.get("dbpassword")
dbhost = os.environ.get("dbhost")
dbname = os.environ.get("dbname")
engine = create_engine(f"mysql+mysqldb://{dbuser}:{dbpassword}@{dbhost}/{dbname}")
Session = sessionmaker(bind=engine)
session = Session()


def listalltasks():
    all_tasks = todo_pb2.AllTasks()
    tasks = session.query(Task).order_by(Task.id)
    # for task in tasks:
        # all_tasks.task.append(todo_pb2.Task(id=task.id, task_todo=task.task_todo, status=task.status))
    return all_tasks


def listallstream():
    tasks = session.query(Task).order_by(Task.id)
    all_tasks = []
    for task in tasks:
        all_tasks.append(
            todo_pb2.Task(id=task.id, task_todo=task.task_todo, status=task.status,)
        )
    return all_tasks


def gettask(request):
    tasks = session.query(Task).filter(Task.id == request.id)
    for task in tasks:
        get_task = task
    task = todo_pb2.Task(
        id=get_task.id, task_todo=get_task.task_todo, status=get_task.status
    )
    return task


def addtask(request):
    task = Task(task_todo=request.task_todo, status=-1)
    session.add(task)
    session.commit()
    return todo_pb2.Empty()


def edittask(request):
    task_to_edit = session.query(Task).filter(Task.id == request.id)
    for task in task_to_edit:
        task.task_todo = request.task_todo
        task.status = request.status
        session.add(task)
        session.commit()
    return todo_pb2.Empty()


def removetask(request):
    task_to_delete = session.query(Task).filter(Task.id == request.id)
    for task in task_to_delete:
        session.delete(task)
        session.commit()
