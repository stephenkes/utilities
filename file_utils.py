# utilities/file_utils.py

def read_file(file_path):
    """Read content from a file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write successful."
    except Exception as e:
        return f"An error occurred: {e}"

