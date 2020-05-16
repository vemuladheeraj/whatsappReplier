import json

import dialogflow
from google.oauth2 import service_account


def dialog_flow_details():
    global session_client, DIALOGFLOW_LANGUAGE_CODE, session
    dialogflow_key = json.load(open("C:\\Users\\vemul\\Downloads\\Dheeraj-ChatBot-2752b0e57277.json"))
    credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))
    session_client = dialogflow.SessionsClient(credentials=credentials)
    # DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
    # DIALOGFLOW_LANGUAGE_CODE = 'en-US'
    # GOOGLE_APPLICATION_CREDENTIALS = 'Dheeraj-ChatBot-2752b0e57277'
    # SESSION_ID = 'current-user-id'
    DIALOGFLOW_LANGUAGE_CODE = 'en-US'
    DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
    SESSION_ID = 'current-user-id'
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
