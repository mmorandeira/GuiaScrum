# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
import rasa_sdk
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
            'None' : "El Scrum Master es el responsable de que Scrum sea entendido y bien aplicado dentro de la organización. Trabaja junto con el Product Owner y el equipo de desarrollo en la creación de valor en cada sprint. Elimina impedimentos y ayuda a ser más productivo al Equipo de desarrollo. \n En cada evento de Scrum el Scrum Master cumple el rol de facilitador, es decir, en una reunión, evento o conversación se encarga de que se cumpla el objetivo de ese espacio, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. Debe ser neutral sobre las decisiones: intervenir sobre el proceso no sobre el resultado. \n 1) En la planificación de la iteración: \n- Trabaja en conjunto con el Product Owner en el refinamiento del Product Backlog.\n- Trabaja con el Product Owner en la creación de las historias de usuario \n- Interviene en caso que no quede claro el objetivo del sprint o alguna característica del producto. \n 2) Durante la ejecución del sprint: \n- Guía al equipo de desarrollo a ser autoorganizado y multifuncional.\n- Remueve impedimentos que pueda tener el equipo de desarrollo durante la ejecución.\n- Facilita eventos de Scrum o espacios de conversación que se requieran durante la etapa. Como por ejemplo las Daily Meetings. \n- Interviene en la Daily Scrum si no se están visibilizando realmente los impedimentos.\n- Ayuda al equipo con la creación y actualización de un Burndown Chart que le permita transparentar el Sprint en curso, inspeccionar y adaptarse. \n- Ayuda al equipo en la preparación de una demo para presentar a los Stakeholders. \n- Maneja un backlog de impedimentos visible para todo el equipo. \n 3) Durante las etapas de revisión y retrospectiva del sprint debe: \n- Organizar una agenda en conjunto con el Product Owner para los diversos Stakeholders. \n- Hacer preguntas a Stakeholders que permitan recibir feedback de valor al equipo. \n- Facilitar la retrospectiva e intervenir mediante preguntas que generen reflexión y perspectiva.\n- Intervenir en la Retrospectiva si se está finalizando sin medidas accionables.",
            'planificacion' : " - Trabajar en conjunto con el Product Owner en el refinamiento del Product Backlog.\n- Trabajar con el Product Owner en la creación de las historias de usuario \n- Intervenir en caso que no quede claro el objetivo del sprint o alguna característica del producto.",
            'daily': "  - Encargarse de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n- Intervenir si considera que no se están visibilizando realmente los impedimentos.",
            'retrospective' : "  - Encargarse de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n- Facilitar la retrospectiva e intervenir mediante preguntas que generen reflexión y perspectiva.\n- Intervenir en la Retrospectiva si se está finalizando sin medidas accionables.",
            'review' : "  - Encargarse de que se cumpla el objetivo de la reunión, que estén disponibles todos los recursos que se necesitan y que todas las voces sean escuchadas. \n- Organizar una agenda en conjunto con el Product Owner para los diversos Stakeholders. \n- Hacer preguntas a Stakeholders que permitan recibir feedback de valor al equipo.",
            'sprint' : "  - Guiar al equipo de desarrollo a ser autoorganizado y multifuncional.\n- Remover impedimentos que pueda tener el equipo de desarrollo durante la ejecución.\n- Facilitar eventos de Scrum o espacios de conversación que se requieran durante la etapa. Como por ejemplo las Daily Meetings. \n- Intervenir en la Daily Scrum si no se están visibilizando realmente los impedimentos.\n- Ayudar al equipo con la creación y actualización de un Burndown Chart que le permita transparentar el Sprint en curso, inspeccionar y adaptarse. \n- Ayudar al equipo en la preparación de una demo para presentar a los Stakeholders. \n- Manejar un backlog de impedimentos visible para todo el equipo."
        }
        message = switcher.get(etapa)
        dispatcher.utter_message(message)
        return [SlotSet('etapa', 'None')]

class ActionTrabajoProductOwner(Action):

    '''
        Esta acción muestra las funciones que realiza el Product Owner en la etapa o evento que solicite el usuario, de no especificar ninguna muestra sus funciones en todas las etapas.
    '''

    def name(self) -> Text:
        return "action_trabajo_product_owner"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        etapa = tracker.get_slot('etapa')
        switcher = {
            'None' : "El Product Owner es el miembro del equipo Scrum responsable de maximizar el valor del producto entregado por el equipo. \n 1) Durante la planificación del proyecto y el sprint debe:\n- Crear la visión del proyecto. Debe formar la visión del proyecto y además crear los límites del presupuesto.\n- Liderar el Sprint Planning. - Organizar el Equipo Scrum, elige quienes participan, colaborará con el plan a desarrollar y también elaborará un plan de trabajo.\n- Crear Épicas. El Product Owner definirá a las personas para abstraerse de algunos usuarios. - Hacer un Backlog priorizado de producto. Favorece ítems de producto que fueron identificados en el Backlog y establece los criterios de aceptación y culminación.\n- Crear un Roadmap (hoja de ruta) de Entregas y duración de Sprint. - Crear las historias del usuario, define su aceptación y proporciona la confirmación de las historias de Usuario con el Equipo Scrum.\n- Identificar las tareas. \n- Diseñar el Sprint Backlog, define los requerimientos del Equipo Scrum y a la vez diseña el Sprint Backlog.\n 2) Durante la ejecución del sprint: \n- Elaborar productos con mayor importancia en el Backlog. \n- Debe participar como un miembro más del Scrum Team para observar cómo trabajan los demás miembros del Scrum Team los procesos. \n 3) Durante las etapas de revisión y retrospectiva del sprint debe: \n- Comprobar y validar Sprints. Está de acuerdo o no con los Entregables; realiza feedback a quien proporciona y al Equipo Scrum; renueva el plan de entrega y el Backlog de los productos. \n- Liberar entregables. Distribuye el producto y coordina con el cliente.\n- Liderar el Sprint Review, debe demostrar y explicar los elementos del Product Blacklog, comentar su estado y hacer un feedback relacionando el estado del mercado en ese momento. \n- Participar en las reuniones de retrospectiva.",
            'planificacion' : "  - Crear la visión del proyecto. Debe formar la visión del proyecto y además crear los límites del presupuesto.\n- Liderar el Sprint Planning. - Organizar el Equipo Scrum, elige quienes participan, colaborará con el plan a desarrollar y también elaborará un plan de trabajo.\n- Crear Épicas. El Product Owner definirá a las personas para abstraerse de algunos usuarios. - Hacer un Backlog priorizado de producto. Favorece ítems de producto que fueron identificados en el Backlog y establece los criterios de aceptación y culminación.\n- Crear un Roadmap (hoja de ruta) de Entregas y duración de Sprint. - Crear las historias del usuario, define su aceptación y proporciona la confirmación de las historias de Usuario con el Equipo Scrum.\n- Identificar las tareas. \n- Diseñar el Sprint Backlog, define los requerimientos del Equipo Scrum y a la vez diseña el Sprint Backlog.\n", 
            'daily': "La asistencia del Product Owner a la reunión diaria no es obligatoria, no está de más que acuda como oyente porque puede facilitar la resolución de impedimentos.",
            'retrospective' : "Reflexionar sobre el último Sprint e identificar posibles mejoras para el próximo.",
            'review' : "Liderar el Sprint Review, debe demostrar y explicar los elementos del Product Blacklog, comentar su estado y hacer un feedback relacionando el estado del mercado en ese momento. \n ",
            'sprint' : "Trabajar con el equipo de desarrollo, manteniendo el enfoque en el objetivo del sprint. \n"
        }
        message = switcher.get(etapa)
        dispatcher.utter_message(message)
        return [SlotSet('etapa', 'None')]

class ActionTrabajoDesarrollador(Action):

    '''
        Esta acción muestra las funciones que realiza el desarrollador en la etapa o evento que solicite el usuario, de no especificar ninguna muestra sus funciones en todas las etapas.
    '''

    def name(self) -> Text:
        return "action_trabajo_desarrollador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        etapa = tracker.get_slot('etapa')
        switcher = {
            'None' : "El Equipo de Desarrollo (o Development Team) se encargar de construir el Incremento de Producto en cada Sprint.\n 1) Durante la planificación del sprint el equipo debe: \n- Seleccionar los Product Backlog Items en los que va a trabajar durante el siguiente Sprint. Estos Product Backlog Items son los que compondrán el Sprint Backlog.\n- Estimar los items del Product Backlog. \n- Se autoorganizan para realizar el trabajo. \n 2) Durante la ejecución del Sprint: \n- Trabajan en conjunto con el Product Owner ajustando el detalle de las funcionalidades planificadas para el sprint. \n- Participan de las Daily Scrum, cada persona del equipo responde a las siguientes preguntas: 1.¿Qué hice ayer para contribuir al Sprint Goal? 2.¿Qué voy a hacer hoy para contribuir al Sprint Goal? 3.¿Tengo algún impedimento que me impida entregar?\n- Llevan a cabo las historias que se comprometieron a realizar durante la planificación. \n 3) En las reuniones de revisión y retrospectiva del sprint: \n- Presentan a los stakeholders el incremento terminado al final del sprint para su inspección y adaptación correspondiente. \n- Comentan que ha ocurrido durante el Sprint, los impedimentos que se han encontrado, así como las soluciones tomadas y actualizan a los stakeholders con la situación del equipo. \n- Reflexionar sobre el último Sprint e identificar posibles mejoras para el próximo.", 
            'planificacion' : "  - Seleccionar los Product Backlog Items en los que va a trabajar durante el siguiente Sprint. Estos Product Backlog Items son los que compondrán el Sprint Backlog.\n- Estimar los items del Product Backlog. \n- Autoorganizarse para realizar el trabajo. \n", 
            'daily': "Cada persona del equipo debe responder a las siguientes preguntas: \n 1.¿Qué hice ayer para contribuir al Sprint Goal?\n 2.¿Qué voy a hacer hoy para contribuir al Sprint Goal?\n 3.¿Tengo algún impedimento que me impida entregar?\n",
            'retrospective' : "Reflexionar sobre el último Sprint e identificar posibles mejoras para el próximo.",
            'review' : "  - Presentar a los stakeholders el incremento terminado al final del sprint para su inspección y adaptación correspondiente. \n- Comentar que ha ocurrido durante el Sprint, los impedimentos que se han encontrado, así como las soluciones tomadas y actualizar a los stakeholders con la situación del equipo. \n",
            'sprint' : "  - Trabajar en conjunto con el Product Owner ajustando el detalle de las funcionalidades planificadas para el sprint. \n- Participar de las Daily Scrum, cada persona del equipo responde a las siguientes preguntas: 1.¿Qué hice ayer para contribuir al Sprint Goal? 2.¿Qué voy a hacer hoy para contribuir al Sprint Goal? 3.¿Tengo algún impedimento que me impida entregar?\n- Llevar a cabo las historias que se comprometieron a realizar durante la planificación. \n"
        }
        message = switcher.get(etapa)
        dispatcher.utter_message(message)
        return [SlotSet('etapa', 'None')]

class ActionBacklog(Action):

    '''
        Esta acción se hizo porque al entrenar el modelo se confundia sprint backlog con product backlog
    '''

    def name(self) -> Text:
        return "action_backlog"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        contexto = tracker.get_slot('contexto')
        switcher = {
            'sprint' : 'Este artefacto es un elemento para visualizar el trabajo a realizar durante cada Sprint y está gestionado por el equipo de desarrollo. Su propósito es mantener la transparencia dentro del desarrollo, actualizándolo durante toda la iteración especialmente a través de los daily Scrums.',
            'product' : 'El Product Backlog es un inventario que contiene cualquier tipo de trabajo que haya que hacer en el producto: requerimientos, casos de uso, tareas y dependencias. Es la principal fuente de información sobre el producto en Scrum, una lista, en cualquier formato, que contiene todos los requerimientos que necesitamos implementar en el producto. El Product Backlog debe ser gestionado en exclusiva por el Product Owner.'
        }    
        message = switcher.get(contexto)
        dispatcher.utter_message(message)
        return [SlotSet('contexto', 'None')]

class ActionPrueba(Action):
    '''
        Esta acción le indica al usuario que tiene que hacer según su rol y fase en la cual se encuentra
    '''
    def name(self) -> Text:
        return "action_que_hacer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rol = tracker.get_slot('rol')
        if rol == 'scrum master':
            return [rasa_sdk.events.FollowupAction('action_trabajo_scrum_master')]
        elif rol == 'product owner':
            return [rasa_sdk.events.FollowupAction('action_trabajo_product_owner')]
        elif rol == 'desarrollador':
            return [rasa_sdk.events.FollowupAction('action_trabajo_desarrollador')]
        else:
            dispatcher.utter_message('El rol ingresado no es válido')

class ActionVerificarRol(Action):

    '''
        Esta acción verifica si se tiene el rol del usuario, sino se lo solicita
    '''

    def name(self) -> Text:
        return "action_verificar_rol"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rol = tracker.get_slot('rol')
        if rol == 'None':
            dispatcher.utter_message('Cual es tu rol?')
        else:
            return [rasa_sdk.events.FollowupAction('action_que_hacer')]