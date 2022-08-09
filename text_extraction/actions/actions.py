# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import io
import requests
import pytesseract
from PIL import Image


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_echo_msg"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        queries=tracker.latest_message['text']
        print(queries)
        
        dispatcher.utter_message(text=queries)

        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "image_text"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities=tracker.latest_message['entities']
        

        response = requests.get(entities)

        img = Image.open(io.BytesIO(response.content))

        i_text = pytesseract.image_to_string(img)

        print(i_text)
        
        dispatcher.utter_message(text=i_text)

        return []

