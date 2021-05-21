# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,AllSlotsReset
from rasa_sdk.events import UserUtteranceReverted


class ActionSetSlotSec(Action):

    def name(self) -> Text:
        return "action_set_perfil_secuencial"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text='setear slot')
        return [SlotSet('perfil', "secuencial")]

class ActionSetSlotInt(Action):

    def name(self) -> Text:
        return "action_set_perfil_intuitivo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text='setear slot')
        return [SlotSet('perfil', "intuitivo")]
