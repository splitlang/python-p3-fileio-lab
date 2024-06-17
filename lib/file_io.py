def write_file(file_name, file_content):
    """
    Writes the provided content to a new text file with the given name.

    Args:
        file_name (str): The name of the file to be created (without the .txt extension).
        file_content (str): The content to be written to the file.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends the provided content to an existing text file with the given name.

    Args:
        file_name (str): The name of the file to be appended (without the .txt extension).
        append_content (str): The content to be appended to the file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads the content of a text file with the given name and returns it as a string.

    Args:
        file_name (str): The name of the file to be read (without the .txt extension).

    Returns:
        str: The content of the file.
    """
    with open(f"{file_name}.txt", "r") as file:
        content = file.read()
    return content