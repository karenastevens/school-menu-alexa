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

def get_cleaned_menu_items(menu_data):
    if menu_data and "ENTREES" in menu_data:
        entrees = menu_data["ENTREES"]
        if entrees:
            cleaned_items = [clean_text(item.get("MenuItemDescription", "")) for item in entrees]
            cleaned_items = [item for item in cleaned_items if item]  # Remove empty strings

            if len(cleaned_items) > 1:
                return ', '.join(cleaned_items[:-1]) + ', and ' + cleaned_items[-1]
            elif cleaned_items:
                return cleaned_items[0]
            else:
                return "the same meals you had yesterday!"
        # Using SSML to slow down the speech rate
            return f"<speak><prosody rate='slow'>{menu_output}</prosody></speak>"
        else:
            return "No entrees found for the selected date."
    else:
        return "I'm not seeing anything for lunch or breakfast today. Check to see if you have a day off school."

# Today's Lunch and Breakfast

class LunchandBreakfastIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchandBreakfastIntent")(handler_input)

    def handle(self, handler_input):
        # Get today's date as a string
        date_str = get_todays_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school today. Have a fantastic weekend!"
        else:
            meal_type = "Breakfast"

            # Fetch the menu data for today's breakfast
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            breakfast_food = get_cleaned_menu_items(menu_data)

            meal_type = 'Lunch'

            # Fetch the menu data for today's lunch
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            lunch_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Today's breakfast is: {breakfast_food}. For lunch tomorrow, you'll be having {lunch_food}." if lunch_food else "I'm sorry, I couldn't find the breakfast and lunch menu for today."
            remprompt_text = "Can I help you with any other menu related questions?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Tomorrow's Lunch and Breakfast

class LunchandBreakfastTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchandBreakfastTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # Get tomorrow's date as a string
        date_str = get_tomorrows_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school tomorrow. Have a fantastic weekend!"
        else:
            meal_type = "Breakfast"

            # Fetch the menu data for tomorrow's breakfast
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            breakfast_food = get_cleaned_menu_items(menu_data)

            meal_type = 'Lunch'

            # Fetch the menu data for tomorrow's lunch
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            lunch_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Tomorrow's breakfast is: {breakfast_food} for lunch tomorrow you'll be having {lunch_food}." if lunch_food else "I'm sorry, I couldn't find the breakfast menu for tomorrow."
            remprompt_text = "Can I help you with any other menu related questions?"


        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Tomorrow's Breakfast

class BreakfastTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BreakfastTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # Get tomorrow's date as a string
        date_str = get_tomorrows_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school tomorrow. Have a fantastic weekend!"
        else:
            meal_type = "Breakfast"

            # Fetch the menu data for tomorrow's lunch
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            breakfast_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Tomorrow's breakfast is: {breakfast_food}" if breakfast_food else "I'm sorry, I couldn't find the breakfast menu for tomorrow."
            remprompt_text = "Do you have any other questions about the breakfast or lunch menu?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Tomorrow's Lunch

class LunchTomorrowIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # Get tomorrow's date as a string
        date_str = get_tomorrows_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school tomorrow. Have a fantastic weekend!"
        else:
            meal_type = "Lunch"

            # Fetch the menu data for tomorrow's lunch
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            lunch_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Tomorrow's lunch is: {lunch_food}" if lunch_food else "I'm sorry, I couldn't find the lunch menu for tomorrow."
            remprompt_text = "Do you have any other questions about the breakfast or lunch menu?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(remprompt_text)
                .response
        )

# Today's Lunch

class LunchIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LunchIntent")(handler_input)

    def handle(self, handler_input):
        # Get today's date as a string
        date_str = get_todays_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school today. Have a fantastic weekend!"
        else:
            meal_type = "Lunch"

            # Fetch the menu data for tomorrow's lunch
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            lunch_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Today's lunch is: {lunch_food}" if lunch_food else "I'm sorry, I couldn't find the lunch menu for today."
            remprompt_text = "Is there anything else I can help you with today?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(remprompt_text)
                .response
        )

# Today's Breakfast

class BreakfastIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BreakfastIntent")(handler_input)

    def handle(self, handler_input):
        # Get today's date as a string
        date_str = get_todays_date()
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if is_weekend(date_obj):
            speak_output = "There is no school today. Have a fantastic weekend!"
        else:
            meal_type = "Breakfast"

            # Fetch the menu data for today's breakfast.
            menu_data = get_menu_data(SCHOOL_ID, date_str, meal_type, GRADE, PERSON_ID)
            # Clean and prepare the menu items for speaking
            breakfast_food = get_cleaned_menu_items(menu_data)

            # Construct the speech output
            speak_output = f"Today's breakfast is: {breakfast_food}" if breakfast_food else "I'm sorry, I couldn't find the breakfast menu for today."
            remprompt_text = "Any other questions about the breakfast and lunch menu at Willow Dale?"

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
