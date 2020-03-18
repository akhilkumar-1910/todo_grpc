from concurrent import futures
import logging
import grpc
# import todo_pb2
import todo_pb2_grpc
from todo_server_fun import listalltasks, listallstream, gettask, addtask, edittask, deletetask


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
        deletetask(request)
        return request


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
