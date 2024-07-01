# test_script.py

from utilities.file_utils import read_file, write_file
from utilities.date_utils import get_current_datetime, format_date

def test_file_utils():
    file_path = 'test.txt'

    # Test writing to a file
    write_result = write_file(file_path, "Hello, world!")
    print(write_result)

    # Test reading from a file
    read_result = read_file(file_path)
    print(read_result)

def test_date_utils():
    # Test getting the current date and time
    current_datetime = get_current_datetime()
    print(f"Current datetime: {current_datetime}")

    # Test formatting the current date
    formatted_date = format_date(current_datetime, "%Y-%m-%d %H:%M:%S")
    print(f"Formatted datetime: {formatted_date}")

if __name__ == "__main__":
    print("Testing file_utils:")
    test_file_utils()

    print("\nTesting date_utils:")
    test_date_utils()
