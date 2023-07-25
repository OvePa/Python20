def get_todos(filepath='todos.txt'):
    """ Read the text file and return the list of todos. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()

    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """ Write a to-to items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
