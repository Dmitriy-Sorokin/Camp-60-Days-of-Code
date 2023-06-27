with open("todo-delete.txt", "r") as file:
    todos = file.readlines()
with open("todo-delete.txt", "w") as file:
    file.writelines(todos)
