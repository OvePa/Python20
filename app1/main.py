while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} -> {item.title()}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        existing_todo = todos[number]
        print(f'Todo to edit: {existing_todo.title()}')
        todos[number] = input('New Todo: ') + '\n'

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todo_removed = todos.pop(number - 1).strip('\n').upper()

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

        message = f'Todo {todo_removed} was removed from the list!'
        print(message)

    elif 'exit' in user_action:
        break
    # case _:
    #    print("Unknown command!")
    else:
        print('Command is not valid!')

print('Bye')
