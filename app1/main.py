todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.lower().strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
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
