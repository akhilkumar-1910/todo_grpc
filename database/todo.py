import os
import grpc
from proto import todo_pb2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from .models.todo import Todo


dbuser = os.environ.get("dbuser")
dbpassword = os.environ.get("dbpassword")
dbhost = os.environ.get("dbhost")
dbname = os.environ.get("dbname")
engine = create_engine(f"mysql+mysqldb://{dbuser}:{dbpassword}@{dbhost}/{dbname}")
Session = sessionmaker(bind=engine)
session = Session()


def list_all_todos():
    all_todos = todo_pb2.AllTodos()
    todos = session.query(Todo).order_by(Todo.id).all()
    for todo in todos:
        all_todos.todo.append(
            todo_pb2.Todo(id=todo.id, content=todo.content, status=todo.status)
        )
    return all_todos


def list_all_stream():
    todos = session.query(Todo).order_by(Todo.id)
    all_todos = []
    for todo in todos:
        all_todos.append(
            todo_pb2.Todo(id=todo.id, content=todo.content, status=todo.status,)
        )
    return all_todos


def get_todo(request, context):
    try:
        get_todo_ = session.query(Todo).filter(Todo.id == request.id).one()
        todo = todo_pb2.Todo(
            id=get_todo_.id, content=get_todo_.content, status=get_todo_.status
        )
        return todo
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return todo_pb2.Todo()


def add_todo(request, context):
    if len(request.content) > 200:
        msg = "Todo cannot be morethan 200 characters"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return todo_pb2.Empty()
    todo = Todo(content=request.content, status=0)
    session.add(todo)
    session.commit()
    return todo_pb2.Empty()


def edit_todo(request, context):
    if len(request.content) > 200:
        msg = "Todo cannot be morethan 200 characters"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return todo_pb2.Empty()
    try:
        todo_to_edit = session.query(Todo).filter(Todo.id == request.id).one()
        todo_to_edit.content = request.content
        todo_to_edit.status = request.status
        session.add(todo_to_edit)
        session.commit()
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return todo_pb2.Empty()
    return todo_pb2.Empty()


def remove_todo(request, context):
    try:
        todo_to_delete = session.query(Todo).filter(Todo.id == request.id).one()
        session.delete(todo_to_delete)
        session.commit()
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)


session.close()
