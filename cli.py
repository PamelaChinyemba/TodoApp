from functions import get_todos, write_todos
import time

now = time.strftime("%d, %b %Y %H:%M:%S")

print(f"It is {now}.")


while True:
    user_action = input("add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].title() + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:].title() + '\n')
            number = (number - 1)

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your code is invalid")
            continue

    elif user_action.startswith('complete'):

        todos = get_todos()
        try:
            number = int(user_action[9:])
            index = number - 1
            item_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {item_to_remove}. Task completed"

            print(message)

        except IndexError:
            print("Index out of range")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('Bye')