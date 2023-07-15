while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.lower().strip():
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
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
