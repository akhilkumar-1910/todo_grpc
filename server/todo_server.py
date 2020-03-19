# from proto import todo_pb2
from proto import todo_pb2_grpc
from .todo_server_fun import listalltasks, listallstream, gettask, addtask, edittask, removetask


class TodoServicer(todo_pb2_grpc.TodoServicer):
    def ListAllTasks(self, request, context):
        all_tasks = listalltasks()
        return all_tasks

    def ListAllStream(self, request, context):
        all_tasks = listallstream()
        for task in all_tasks:
            yield task

    def GetTask(self, request, context):
        task = gettask(request)
        return task

    def AddTask(self, request, context):
        new_task = addtask(request)
        return new_task

    def EditTask(self, request, context):
        edited_task = edittask(request)
        return edited_task

    def RemoveTask(self, request, context):
        removetask(request)
        return request
