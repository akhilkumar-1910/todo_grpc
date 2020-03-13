from __future__ import print_function
import logging
import os
import grpc
import todo_pb2
import todo_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        while 1:
            os.system("clear")
            print("Listing all todos: ")
            all_todos = stub.ListAllTasks(todo_pb2.Empty())
            for p in all_todos.task:
                print(f"{p.id} {p.task_todo}, status: {p.status} (-1: not completed, 1: completed)")
            all_todos = stub.ListAllStream(todo_pb2.Empty())
            for p in all_todos:
                print(f"{p.id} {p.task_todo}, status: {p.status} (-1: not completed, 1: completed)")
            print("\nCommand line todo application. Select one of the following options: ")
            print("1. Add a todo")
            print("2. Edit a todo")
            print("3. Remove a todo")
            print("4. Update the status of a todo")
            option = input("\nPlease enter the option: ")
            if option == '1':
                content = input("Please enter the task todo: ")
                task = todo_pb2.Task(task_todo=content)
                response = stub.AddTask(task)
                print(f"{response.task_todo} added succesfully")
            elif option == '2':
                edit_id = input("Please enter the id of the task to edit: ")
                edit_content = input("Please enter the content of new task: ")
                task = todo_pb2.Task(id=int(edit_id), task_todo=edit_content, status=-1)
                edit_task_response = stub.EditTask(task)
                print(f"{edit_task_response.task_todo} updated succesfully")
            elif option == '3':
                del_id = input("Please enter the id of the task to delete: ")
                task = todo_pb2.Task(id=int(del_id))
                resp = stub.RemoveTask(task)
                print(f"{resp.id} removed succesfully")
            elif option == '4':
                update_id = input("Please enter the id of the task to update status: ")
                updated_status = input("Enter updated status 1 for complete -1 for imcomplete: ")
                task = todo_pb2.Task(id=int(update_id), status=int(updated_status))
                resp = stub.UpdateStatus(task)
                print(f"{resp.id} status updated succesfully")


if __name__ == '__main__':
    logging.basicConfig()
    run()
