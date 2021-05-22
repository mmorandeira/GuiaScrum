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

class ActionTrabajoScrumMaster(Action):

    '''
        Esta acción muestra las funciones que realiza el Scrum Master en la etapa o evento que solicite el usuario, de no especificar ninguna muestra sus funciones en todas las etapas.
    '''

    def name(self) -> Text:
        return "action_trabajo_scrum_master"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        etapa = tracker.get_slot('etapa')
        switcher = {
            'None' : "El Scrum Master es el responsable de que Scrum sea entendido y bien aplicado dentro de la organización. Trabaja junto con el Product Owner y el equipo de desarrollo en la creación de valor en cada sprint. Elimina impedimentos y ayuda a ser más productivo al Equipo de desarrollo. \n En cada evento de Scrum el Scrum Master cumple el rol de facilitador, es decir, en una reunión, evento o conversación se encarga de que se cumpla el objetivo de ese espacio, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. Debe ser neutral sobre las decisiones: intervenir sobre el proceso no sobre el resultado. \n 1) En la planificación de la iteración: \n - Trabaja en conjunto con el Product Owner en el refinamiento del Product Backlog.\n - Trabaja con el Product Owner en la creación de las historias de usuario \n - Interviene en caso que no quede claro el objetivo del sprint o alguna característica del producto. \n 2) Durante la ejecución del sprint: \n - Guía al equipo de desarrollo a ser autoorganizado y multifuncional.\n - Remueve impedimentos que pueda tener el equipo de desarrollo durante la ejecución.\n - Facilita eventos de Scrum o espacios de conversación que se requieran durante la etapa. Como por ejemplo las Daily Meetings. \n - Interviene en la Daily Scrum si no se están visibilizando realmente los impedimentos.\n - Ayuda al equipo con la creación y actualización de un Burndown Chart que le permita transparentar el Sprint en curso, inspeccionar y adaptarse. \n - Ayuda al equipo en la preparación de una demo para presentar a los Stakeholders. \n - Maneja un backlog de impedimentos visible para todo el equipo. \n 3) Durante las etapas de revisión y retrospectiva del sprint debe: \n - Organizar una agenda en conjunto con el Product Owner para los diversos Stakeholders. \n - Hacer preguntas a Stakeholders que permitan recibir feedback de valor al equipo. \n - Facilitar la retrospectiva e intervenir mediante preguntas que generen reflexión y perspectiva.\n - Intervenir en la Retrospectiva si se está finalizando sin medidas accionables.",
            'planificacion' : " - Trabaja en conjunto con el Product Owner en el refinamiento del Product Backlog.\n - Trabaja con el Product Owner en la creación de las historias de usuario \n - Interviene en caso que no quede claro el objetivo del sprint o alguna característica del producto.",
            'daily': " - Se encarga de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n - Interviene si considera que no se están visibilizando realmente los impedimentos.",
            'retrospective' : " - Se encarga de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n - Facilitar la retrospectiva e intervenir mediante preguntas que generen reflexión y perspectiva.\n - Intervenir en la Retrospectiva si se está finalizando sin medidas accionables.",
            'review' : " - Se encarga de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n - Organizar una agenda en conjunto con el Product Owner para los diversos Stakeholders. \n - Hacer preguntas a Stakeholders que permitan recibir feedback de valor al equipo.",
            'sprint' : " - Guía al equipo de desarrollo a ser autoorganizado y multifuncional.\n - Remueve impedimentos que pueda tener el equipo de desarrollo durante la ejecución.\n - Facilita eventos de Scrum o espacios de conversación que se requieran durante la etapa. Como por ejemplo las Daily Meetings. \n - Interviene en la Daily Scrum si no se están visibilizando realmente los impedimentos.\n - Ayuda al equipo con la creación y actualización de un Burndown Chart que le permita transparentar el Sprint en curso, inspeccionar y adaptarse. \n - Ayuda al equipo en la preparación de una demo para presentar a los Stakeholders. \n - Maneja un backlog de impedimentos visible para todo el equipo."
        }
        message = switcher.get(etapa)
        dispatcher.utter_message(message)
        return [SlotSet('etapa', 'None')]