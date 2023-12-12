import logging
import requests
import json
import boto3
from datetime import date, datetime, timedelta
import re
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Global constants - specific to each school
SCHOOL_ID = "9fd858fc-357b-44be-8652-07f574f659d3" # Willow Dale Elementary
GRADE = "04" # Student grade
PERSON_ID = "4eb64127-3ea4-4c3d-91ac-b8035a3971f7" # Student Schoolcafe ID

# Utility functions

def get_todays_date():
    today = datetime.now()
    return today.strftime("%Y-%m-%d")

def get_tomorrows_date():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    return tomorrow.strftime("%Y-%m-%d")

def is_weekend(date):
    return date.weekday() >= 5

# Text cleaning function to make it easier for Alexa to read
def clean_text(text):
    # Replace or remove unwanted characters and words
    text = text.replace('w/', ' with ')
    text = text.replace('&', 'and')
    text = text.replace('Combo', '')  # Remove the word 'combo'
    text = text.replace('Meal', '')   # Remove the word 'meal'
    text = text.replace('ES', '')     # Remove the word 'ES'
    text = re.sub(r'\d+', '', text)   # Remove all numbers
    text = text.replace('#', '')
    text = text.replace('Main', '')
    return text.strip()  # Remove any leading/trailing whitespace

def get_menu_data(school_id, date, meal_type, grade, person_id):
    # Construct the API URL for Schoolcafe
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

    # Make the request
    response = requests.get(base_url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error fetching data: {response.status_code}")
        logger.error("Response content: " + response.text)
        return None

def get_cleaned_menu_items(menu_data):
    if menu_data and "ENTREES" in menu_data:
        entrees = menu_data["ENTREES"]
        if entrees:  # Check if there are any items in ENTREES
            cleaned_items = [clean_text(item.get("MenuItemDescription", "")) for item in entrees]
            return ', '.join(cleaned_items)
        else:
            return "No entrees found for the selected date."
    else:
        return "No data received."


class LunchandBreakfastIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchandBreakfastIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Today's breakfast will be {breakfast_food} and for lunch you are having {lunch_food}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class LunchandBreakfastTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchandBreakfastTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Tomorrow's breakfast will be {breakfast_food_tomorrow}. And for lunch tomorrow you will be having {lunch_food_tomorrow}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class BreakfastTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BreakfastTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Tomorrow's breakfast is {breakfast_food_tomorrow}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class LunchTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Tomorrow's lunch is {lunch_food_tomorrow}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class LunchIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Today's lunch is {lunch_food}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class BreakfastIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BreakfastIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = f"Today's breakfast is {breakfast_food}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hey there! Feel free to ask me what's for breakfast or lunch and I can tell you what is being served at Willow Dale Elementary!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can ask me what's for breakfast and lunch for today and tomorrow! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye! Feel free to visit the Willow Dale Menu any day!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can ask what's for breakfast or lunch. If you need more help say help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(LunchandBreakfastTomorrowIntentHandler())
sb.add_request_handler(LunchandBreakfastIntentHandler())
sb.add_request_handler(BreakfastTomorrowIntentHandler())
sb.add_request_handler(LunchTomorrowIntentHandler())
sb.add_request_handler(LunchIntentHandler())
sb.add_request_handler(BreakfastIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
