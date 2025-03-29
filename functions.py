FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """

    :param filepath: takes the name of the file as argument
    :return: reads the contents of  the files, stores in a list and returns that list with name todos_local
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH, ):
    """

    :param filepath: filepath of  the file
    :param todos_arg: todos list to be written to the file which has been entered by the user
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")