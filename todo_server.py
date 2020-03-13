from concurrent import futures
import logging
import grpc
import todo_pb2
import todo_pb2_grpc


class TodoServicer(todo_pb2_grpc.TodoServicer):

    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def ListAllTasks(self, request, context):
        all_tasks = todo_pb2.AllTasks()
        for k in sorted(self.tasks):
            all_tasks.task.append(self.tasks[k])
        return all_tasks

    def ListAllStream(self, request, context):
        for k in sorted(self.tasks):
            task = todo_pb2.Task(id=self.tasks[k].id, task_todo=self.tasks[k].task_todo,
                                 status=self.tasks[k].status)
            yield task

    def AddTask(self, request, context):
        new_task = todo_pb2.Task(id=self.counter, task_todo=request.task_todo, status=-1)
        self.tasks[self.counter] = new_task
        self.counter = self.counter+1
        print(self.tasks)
        return new_task

    def EditTask(self, request, context):
        self.tasks[request.id] = request
        return self.tasks[request.id]

    def RemoveTask(self, request, context):
        del self.tasks[request.id]
        return request

    def UpdateStatus(self, request, context):
        self.tasks[request.id].status = request.status
        return self.tasks[request.id]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(
        TodoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
