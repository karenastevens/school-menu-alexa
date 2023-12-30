import requests
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

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
