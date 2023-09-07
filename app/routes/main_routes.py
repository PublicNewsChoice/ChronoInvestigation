from datetime import datetime

def format_datetime(value):
    """
    Formats a datetime object to a more readable string format
    """
    return value.strftime('%Y-%m-%d %H:%M:%S')
