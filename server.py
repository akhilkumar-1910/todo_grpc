import logging
from concurrent import futures
import grpc
from proto import todo_pb2_grpc
from server.server import TodoAppServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoAppServicer_to_server(TodoAppServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
