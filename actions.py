# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class MailForm(Action):

    def name(self) -> Text:
        return "action_send_mailtouser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import smtplib
                
        dispatcher.utter_message(text="sending email")
        body = "Hello..  For more details please visit our website"
        sender_email = "butchi.vattepollu@gmail.com"
        receiver_email = "vijaynathgundala@gmail.com"
        password = "pavan777"
        
        s = smtplib.SMTP(host='smtp.office365.com', port=587)
        s.starttls()
        s.login(sender_email, password)
        s.sendmail(sender_email, receiver_email, body)
        
        dispatcher.utter_message(text="email sent")

        return []
    
