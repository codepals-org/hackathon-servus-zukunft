# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import json


class ActionOrderDrink(Action):

    def name(self) -> Text:
        return "action_order_drink"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            drink_type = [entity['value'] for entity in tracker.latest_message['entities'] if entity['entity']=='drink'][0]
        except IndexError:
            drink_type = None
        try:
            drink_size = [entity['value'] for entity in tracker.latest_message['entities'] if entity['entity']=='size'][0]
        except IndexError:
            drink_size = None

        if drink_type not in ['Bier', 'Spezi', 'Apfelschorle']:
            dispatcher.utter_message(f"{drink_type} ist leider nicht verfügbar. Wähle:")
            dispatcher.utter_message(buttons = [
            {"payload": '/order{{"drink":"{Bier}"}}', "title": "Bier"},
            {"payload": '/order{{"drink":"{Bier}"}}', "title": "Spezi"},
            {"payload": '/order{{"drink":"{Apfelschorle}"}}', "title": "Apfelschorle"}
            ])

        elif drink_size not in ['1 Liter', '0.5 Liter']:
            dispatcher.utter_message(f"Größe {drink_size} ist leider nicht verfügbar.")
            dispatcher.utter_message(buttons = [
            {"payload": '/order{{"drink":"{0.5 Liter}"}}', "title": "0.5 Liter"},
            {"payload": '/order{{"drink":"{1 Liter}"}}', "title": "1 Liter"}
            ])

        else:
            dispatcher.utter_message(text=f"Du hast ein {drink_type} in Größe {drink_size} bestellt.")

        return []

class ActionQueryTemperature(Action):

    def name(self) -> Text:
        return "action_query_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Dein Bier ist warm!")

        return []

class ActionQueryWeight(Action):

    def name(self) -> Text:
        return "action_query_weight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('/home/sarah/code/bierbot/rasa_project/sample_data.json') as file:
            mock_data = json.load(file)
            weight = mock_data['weight']

        drink_type = [entity['value'] for entity in tracker.latest_message['entities'] if entity['entity']=='drink'][0]
        if not drink_type:
            drink_type = 'Getränk'
        
        if weight < 100:            
            dispatcher.utter_message(text=f"Dein {drink_type} ist fast leer! Nur noch {weight} Milliliter.")
            dispatcher.utter_message(text="Möchtest du ein neues bestellen?")
            dispatcher.utter_message(buttons = [
                    {"payload": f'/order\u007b\u007b"drink":"{drink_type}"\u007d\u007d', "title": "Ja"},
                    {"payload": "/mood_unhappy", "title": "Nein"},
                ])

        if weight >= 100:
            dispatcher.utter_message(text=f"Du hast noch {weight} Milliliter Bier.")

        print()
        return []