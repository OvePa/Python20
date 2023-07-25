from functions import get_todos,write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} -> {item.title()}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            existing_todo = todos[number]
            print(f'Todo to edit: {existing_todo.title()}')
            todos[number] = input('New Todo: ') + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid!")
            continue
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_removed = todos.pop(number - 1).strip('\n').upper()

            write_todos(todos)

            message = f'Todo {todo_removed} was removed from the list!'
            print(message)
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break
    # case _:
    #    print("Unknown command!")
    else:
        print('Command is not valid!')

print('Bye')
