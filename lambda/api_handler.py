import requests
import logging
import utils
from dotenv import load_dotenv
import os

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv()

# Variables will be specific to school and student and has to be set in environment.

SCHOOL_ID = os.getenv('SCHOOL_ID')
GRADE = os.getenv('GRADE')
PERSON_ID = os.getenv('PERSON_ID')

def get_menu_data(school_id, date, meal_type, grade, person_id):
    """
    Fetches menu data from the Schoolcafe API for a given school, date, and meal type.

    Args:
        school_id (str): The ID of the school.
        date (str): The date for which to fetch the menu, in 'YYYY-MM-DD' format.
        meal_type (str): The type of meal, e.g., 'Breakfast' or 'Lunch'.
        grade (str): The grade level.
        person_id (str): The ID of the person.

    Returns:
        dict or None: The menu data if successful, None otherwise.
    """
    base_url = "https://webapis.schoolcafe.com/api/CalendarView/GetDailyMenuitemsByGrade"
    params = {
        "SchoolId": school_id,
        "ServingDate": date,
        "ServingLine": "Regular",
        "MealType": meal_type,
        "Grade": grade,
        "PersonId": person_id
    }
    headers = {
        "accept": "application/json"
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error fetching data: {response.status_code}")
        logger.error("Response content: " + response.text)
        return None

def get_cleaned_menu_items(menu_data):
    """
    Processes and cleans the menu data for Alexa's response.

    Args:
        menu_data (dict): The raw menu data from the API.

    Returns:
        str: A cleaned and formatted string of menu items.
    """
    if menu_data and "ENTREES" in menu_data:
        entrees = menu_data["ENTREES"]
        if entrees:
            cleaned_items = [utils.clean_text(item.get("MenuItemDescription", "")) for item in entrees]
            cleaned_items = [item for item in cleaned_items if item]  # Remove empty strings

            if len(cleaned_items) > 1:
                return ', '.join(cleaned_items[:-1]) + ', and ' + cleaned_items[-1]
            elif cleaned_items:
                return cleaned_items[0]
            else:
                return "the same meals you had yesterday!"
        else:
            return "No entrees found for the selected date."
    else:
        return "I'm not seeing anything for lunch or breakfast today. Check to see if you have a day off school."
