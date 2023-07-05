todos = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action.lower().strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                x = 1
                print(x, item.title())
                x = x + 1
        case 'exit':
            break
        # case _:
        #    print("Unknown command!")

print('Bye')
