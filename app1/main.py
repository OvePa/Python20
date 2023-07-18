def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()

    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

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

            todo= get_todos()

            existing_todo = todos[number]
            print(f'Todo to edit: {existing_todo.title()}')
            todos[number] = input('New Todo: ') + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
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

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

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
