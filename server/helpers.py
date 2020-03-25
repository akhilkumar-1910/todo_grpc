from database import todo

"""
Helper functions for server.py
"""


def list_all_todos():
    all_todos = todo.list_all_todos()
    return all_todos


def list_all_stream():
    all_todos = todo.list_all_stream()
    return all_todos


def get_todo(request, context):
    return todo.get_todo(request, context)


def add_todo(request, context):
    return todo.add_todo(request, context)


def edit_todo(request, context):
    return todo.edit_todo(request, context)


def remove_todo(request, context):
    return todo.remove_todo(request, context)
