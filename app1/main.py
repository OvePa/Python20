todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action.lower().strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            x = 1
            for item in todos:
                print(x, item.title())
                x = x + 1
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            existing_todo = todos[number]
            print('Todo to edit: ',existing_todo.title())
            todos[number] = input('New Todo: ')
        case 'exit':
            break
        # case _:
        #    print("Unknown command!")

print('Bye')
