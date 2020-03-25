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
    """
    Lists all the todos from the databases

    Args:
        No args

    Returns:
        all_todos: A todo_pb2.AllTodos object
    """
    all_todos = todo_pb2.AllTodos()
    todos = session.query(Todo).order_by(Todo.id).all()
    for todo in todos:
        all_todos.todo.append(
            todo_pb2.Todo(id=todo.id, content=todo.content, status=todo.status)
        )
    return all_todos


def list_all_stream():
    """
    Lists all the todos from the databases

    Args:
        No args

    Returns:
        all_todos(list): A list of todo_pb2.Todo objects
    """
    todos = session.query(Todo).order_by(Todo.id)
    all_todos = []
    for todo in todos:
        all_todos.append(
            todo_pb2.Todo(id=todo.id, content=todo.content, status=todo.status,)
        )
    return all_todos


def get_todo(request, context):
    """
    Lists a todo based on the id of the todo

    Args:
        request(todo_pb2.Todo object): for getting id
        context(grpc.ServicerContext): for setting error code and details

    Returns:
        todo(todo_pb2.Todo object): returns a todo object with given id
            returns a empty todo object if id not found in the database

    Raises:
        sqlalchemy.orm.exc.NoResultFound: If no todo object is found with given id
    """
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
    """
    Adds a todo to database

    Args:
        request(todo_pb2.Todo object): for getting id
        context(grpc.ServicerContext): for setting error code and details

    Returns:
        todo(todo_pb2.Empty object): returns a todo_pb2.Empty object
    """
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
    """
    Edits a todo based on the id of the todo

    Args:
        request(todo_pb2.Todo object): for getting id
        context(grpc.ServicerContext): for setting error code and details

    Returns:
        todo(todo_pb2.Empty object): returns a todo_pb2.Empty object

    Raises:
        sqlalchemy.orm.exc.NoResultFound: If no todo object is found with given id
    """
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
    """
    Edits a todo based on the id of the todo

    Args:
        request(todo_pb2.Todo object): for getting id
        context(grpc.ServicerContext): for setting error code and details

    Raises:
        sqlalchemy.orm.exc.NoResultFound: If no todo object is found with given id
    """
    try:
        todo_to_delete = session.query(Todo).filter(Todo.id == request.id).one()
        session.delete(todo_to_delete)
        session.commit()
    except NoResultFound:
        msg = "No task found with the given id"
        context.set_details(msg)
        context.set_code(grpc.StatusCode.NOT_FOUND)


session.close()
