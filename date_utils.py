# utilities/date_utils.py

from datetime import datetime

def get_current_datetime():
    """Get the current date and time."""
    return datetime.now()

def format_date(date, format_string="%Y-%m-%d"):
    """Format a date according to the provided format string."""
    try:
        return date.strftime(format_string)
    except Exception as e:
        return f"An error occurred: {e}"
