from proto import todo_pb2
from sqlalchemy import create_engine
from models.todo_sqlalchemy import Task
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import grpc
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
    tasks = session.query(Task).order_by(Task.id).all()
    for task in tasks:
        all_tasks.task.append(
            todo_pb2.Task(id=task.id, task_todo=task.task_todo, status=task.status)
        )
    return all_tasks


def listallstream():
    tasks = session.query(Task).order_by(Task.id)
    all_tasks = []
    for task in tasks:
        all_tasks.append(
            todo_pb2.Task(id=task.id, task_todo=task.task_todo, status=task.status,)
        )
    return all_tasks


def gettask(request, context):
    try:
        get_task = session.query(Task).filter(Task.id == request.id).one()
        task = todo_pb2.Task(
            id=get_task.id, task_todo=get_task.task_todo, status=get_task.status
        )
        return task
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return todo_pb2.Task()


def addtask(request, context):
    if len(request.task_todo) > 200:
        msg = "Task cannot be morethan 200 characters"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return todo_pb2.Empty()
    task = Task(task_todo=request.task_todo, status=-1)
    session.add(task)
    session.commit()
    return todo_pb2.Empty()


def edittask(request, context):
    if len(request.task_todo) > 200:
        msg = "Task cannot be morethan 200 characters"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return todo_pb2.Empty()
    try:
        task_to_edit = session.query(Task).filter(Task.id == request.id).one()
        task_to_edit.task_todo = request.task_todo
        task_to_edit.status = request.status
        session.add(task_to_edit)
        session.commit()
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return todo_pb2.Empty()
    return todo_pb2.Empty()


def removetask(request, context):
    try:
        task_to_delete = session.query(Task).filter(Task.id == request.id).one()
        session.delete(task_to_delete)
        session.commit()
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)
