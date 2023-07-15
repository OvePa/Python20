while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.lower().strip():
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1} -> {item.title()}")

        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            existing_todo = todos[number]
            print('Todo to edit: ', existing_todo.title())
            todos[number] = input('New Todo: ')
        case 'complete':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            todos.pop(number)

        case 'exit':
            break
        # case _:
        #    print("Unknown command!")

print('Bye')
