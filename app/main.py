import requests
import os
import json

DESCRIPTOR = '$ '

API_GATEWAY_URL = "http://localhost:5000"
login_id = None

def login(username, password):
    global login_id
    data = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(f"{API_GATEWAY_URL}/login", json=data)
        if response.ok:
            print("success!!")
            login_id = response.json()['user_id']

        else:
            print(f"Login failed: {response.json().get('error', 'Unkown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")



def register(username, password):
    data = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(f"{API_GATEWAY_URL}/register", json=data)
        if response.ok:
            print(response.text)
        else:
            print(f"Register failed: {response.json().get('error', 'Unkown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

def create_task(task):
    pass

def list_tasks():
    try:
        response = requests.get(f"{API_GATEWAY_URL}/tasks/{login_id}")
        if response.ok:
            print("ye")
        else:
            print(f"Register failed: {response.json().get('error', 'Unkown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

def complete_task(task):
    pass

def delete_task(task):
    pass


if __name__ == '__main__':
    # Login loop
    while (login_id == None):
        print(
            "Welcome to Taskinator3000!\n" +
            "Login or register to use the system!\n" +
            "Type either of the following commands!\n"
            "---) login\n" +
            "---) register\n" + 
            "---) q (to exit)\n"
            )

        input_string = input(DESCRIPTOR)
        input_strings = input_string.split(' ')
        cmd = input_strings[0]
        args = input_strings[1:]

        match cmd.lower():
            case "login":
                if len(args) != 2:
                    print("Error! incorrect amount of arguments, expects 2 got " + str(len(args)))
                else:
                    login(args[0], args[1])
            case "register":
                if len(args) != 2:
                    print("Error! incorrect amount of arguments, expects 2 got " + str(len(args)))
                else:
                    register(args[0], args[1])
            case "q":
                exit(0)
            case _:
                print("Error! incorrect command!")

    # task loop
    while (True):
        print(
            "Welcome to the terminal!\n" +
            "interact with the system by typing one of the commands below\n" +
            "---) cr <task> (creates task)\n" +
            "---) complete <task_id> (completes task)\n" + 
            "---) ls (lists all tasks)\n" + 
            "---) del <task_id> (deletes task)"
            "---) q (to exit)\n"
            )

        input_string = input(DESCRIPTOR)
        input_strings = input_string.split(' ')
        cmd = input_strings[0]
        args = input_strings[1:]

        match cmd.lower():
            case "cr":
                if len(args) != 1:
                    print("Error! incorrect amount of arguments, expects 1 got " + str(len(args)))
                else:
                    create_task(args[0])
            case "complete":
                if len(args) != 1:
                    print("Error! incorrect amount of arguments, expects 1 got " + str(len(args)))
                else:
                    create_task(args[0])
            case "ls":
                    list_tasks()
            case "del":
                if len(args) != 1:
                    print("Error! incorrect amount of arguments, expects 1 got " + str(len(args)))
                else:
                    create_task(args[0])
            case "q":
                exit(0)
            case _:
                print("Error! incorrect command!")