if __name__ == "__main__":
    todo_list = []
    redo_list = []

    while True:
        print("1 - adicionar tarefa")
        print("2 - listar")
        print("3 - undo")
        print("4 - redo")
        todo = input("Enter a option: ")
        if todo == "1":
            todo_list.append(input("Enter a task: "))
        elif todo == "2":
            for x in todo_list:
                print("#" * 20)
                print(x)
                print("#" * 20)
        elif todo == "3":
            if len(todo_list) > 0:
                redo_list.append(todo_list.pop())
        elif todo == "4":
            if len(redo_list) > 0:
                todo_list.append(redo_list.pop())
