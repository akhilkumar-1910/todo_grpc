from __future__ import print_function
import os
import grpc
# from proto import todo_pb2
from proto import todo_pb2_grpc
from .todo_client_fun import listalltasks, addtask, edittask, removetask


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        while True:
            os.system("clear")
            try:
                listalltasks(stub)
            except grpc.RpcError as e:
                print(e.details())
                print(e.code())
                break
            print(
                "\nCommand line todo application. Select one of the following options: "
            )
            print("1. Add a todo")
            print("2. Edit a todo")
            print("3. Remove a todo")
            print("4. Update the status of a todo")
            print("5. Exit")
            option = input("\nPlease enter the option: ")
            if option == "1":
                try:
                    addtask(stub)
                except grpc.RpcError as e:
                    print(e.details())
            elif option == "2":
                try:
                    edittask(stub, option)
                except grpc.RpcError as e:
                    print(e.details())
            elif option == "3":
                try:
                    removetask(stub)
                except grpc.RpcError as e:
                    print(e.details())
            elif option == "4":
                try:
                    edittask(stub, option)
                except grpc.RpcError as e:
                    print(e.details())
            elif option == "5":
                break
            else:
                print("Please enter a valid input")
            input("Input enter to continue ...")
