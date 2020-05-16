import json

import dialogflow
from google.oauth2 import service_account


class DialogFlowAccessDetails:
    def __init__(self):
        # global session_client, DIALOGFLOW_LANGUAGE_CODE, session
        self.dialogflow_key = json.load(open("C:\\Users\\vemul\\Downloads\\Dheeraj-ChatBot-2752b0e57277.json"))
        self.credentials = (service_account.Credentials.from_service_account_info(self.dialogflow_key))
        self.session_client = dialogflow.SessionsClient(credentials=self.credentials)
        # DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
        # DIALOGFLOW_LANGUAGE_CODE = 'en-US'
        # GOOGLE_APPLICATION_CREDENTIALS = 'Dheeraj-ChatBot-2752b0e57277'
        # SESSION_ID = 'current-user-id'
        self.DIALOGFLOW_LANGUAGE_CODE = 'en-US'
        self.DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
        self.SESSION_ID = 'current-user-id'
        self.session = self.session_client.session_path(self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID)


def dialog_flow_details():
    return DialogFlowAccessDetails()
