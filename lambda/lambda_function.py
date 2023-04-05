# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import json
import boto3
from datetime import date, datetime, timedelta
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Initialize S3 client
s3 = boto3.client('s3')

# Specify the S3 bucket name and file paths
bucket_name = 'your-bucket-name'
breakfast_file_key = 'breakfast_menu_file_path'
lunch_file_key = 'lunch_menu_file_path'

# Retrieve the objects from the S3 bucket
breakfast_object = s3.get_object(Bucket=bucket_name, Key=breakfast_file_key)
lunch_object = s3.get_object(Bucket=bucket_name, Key=lunch_file_key)

# Load the JSON data from the objects
breakfast_food_list = json.load(breakfast_object['Body'])
lunch_food_list = json.load(lunch_object['Body'])

# Get the current date
today = date.today()

tomorrow = tomorrow = today + timedelta(days=1)

# Get the dictionary with the matching date for breakfast today
matching_item = next((item for item in breakfast_food_list if datetime.strptime(item['Date'], "%Y-%m-%d").date() == today), None)

# Check if a matching dictionary was found
if matching_item:
  # Print the corresponding food
    breakfast_food = matching_item['Food']

# Get the dictionary with the matching date for lunch today
matching_item = next((item for item in lunch_food_list if datetime.strptime(item['Date'], "%Y-%m-%d").date() == today), None)

if matching_item:
  # Print the corresponding food
    lunch_food = matching_item['Food']

# Get the dictionary with the matching date for breakfast tomorrow
matching_item = next((item for item in breakfast_food_list if datetime.strptime(item['Date'], "%Y-%m-%d").date() == tomorrow), None)

# Check if a matching dictionary was found
if matching_item:
  # Print the corresponding food
    breakfast_food_tomorrow = matching_item['Food']

# Get the dictionary with the matching date for lunch tomorrow
    matching_item = next((item for item in lunch_food_list if datetime.strptime(item['Date'], "%Y-%m-%d").date() == tomorrow), None)

if matching_item:
  # Print the corresponding food
    lunch_food_tomorrow = matching_item['Food']

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
