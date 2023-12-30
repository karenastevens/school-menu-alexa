from datetime import datetime, timedelta
import re

def get_todays_date():
    """
    Returns the current date in 'YYYY-MM-DD' format.

    Returns:
        str: The current date.
    """
    today = datetime.now()
    return today.strftime("%Y-%m-%d")

def get_tomorrows_date():
    """
    Returns tomorrow's date in 'YYYY-MM-DD' format.

    Returns:
        str: Tomorrow's date.
    """
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    return tomorrow.strftime("%Y-%m-%d")

def is_weekend(date):
    """
    Checks if a given date is a weekend.

    Args:
        date (datetime.date): The date to check.

    Returns:
        bool: True if the date is a weekend, False otherwise.
    """
    return date.weekday() >= 5

def clean_text(text):
    """
    Cleans the given text for better readability by Alexa.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = text.replace('w/', ' with ')
    text = text.replace('&', 'and')
    text = text.replace('Combo', '')  # Remove the word 'combo'
    text = text.replace('Meal', '')   # Remove the word 'meal'
    text = text.replace('ES', '')     # Remove the word 'ES'
    text = re.sub(r'\d+', '', text)   # Remove all numbers
    text = text.replace('#', '')
    text = text.replace('Main', '')
    return text.strip()  # Remove any leading/trailing whitespace
