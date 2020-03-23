from __future__ import print_function
import os
import grpc

# from proto import todo_pb2
from proto import todo_pb2_grpc
from .helpers import list_all_todos, add_todo, edit_todo, remove_todo


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.TodoAppStub(channel)
        while True:
            os.system("clear")
            try:
                list_all_todos(stub)
            except grpc.RpcError:
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
                add_todo(stub)
            elif option == "2":
                edit_todo(stub, option)
            elif option == "3":
                remove_todo(stub)
            elif option == "4":
                edit_todo(stub, option)
            elif option == "5":
                break
            else:
                print("Please enter a valid input")
            input("Input enter to continue ...")
