import datetime
import json
import time

import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\vemul\PycharmProjects\whatsappReplier\Debug Files")
# options.binary_location="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="D:\Selenium Learning\chromedriver_win32 (2)\chromedriver.exe",
                          options=options)
driver.get("https://web.whatsapp.com/")
driver.fullscreen_window()
last_message_User = {}
mycontacts = ['Sister']
for name in mycontacts:
    last_message_User[name] = ""
wait = WebDriverWait(driver, 5000)
wait.until(EC.element_to_be_clickable((By.ID, "side")))
SystemLastDefaultMessage = "DefaultMessage"


def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


for contact in mycontacts:
    driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").clear()
    driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(contact)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    lastMessageReceivedwithTime = driver.find_element_by_xpath(
        "//*[contains(@class,'message-in focusable-list-item')][last()]").text
    Temp_lastMessageReceived = lastMessageReceivedwithTime.split("\n")[0]
    last_message_User[contact] = Temp_lastMessageReceived
    before_loop_date_time = datetime.datetime.now().time()
    loop_break_time = addSecs(before_loop_date_time, 60)
    while True:
        current_last_message_received = \
            driver.find_element_by_xpath("//*[contains(@class,'message-in focusable-list-item')][last()]").text.split(
                "\n")[
                0]
        if current_last_message_received != last_message_User.get(contact):
            text_to_be_analyzed = current_last_message_received
            last_message_User[contact] = current_last_message_received
            text_input = dialogflow.types.TextInput(text=text_to_be_analyzed,
                                                    language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)
            try:
                response = session_client.detect_intent(session=session, query_input=query_input)
            except InvalidArgument:
                raise
            responseForMessage = response.query_result.fulfillment_text
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(
                responseForMessage)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(
                Keys.ENTER)
            before_loop_date_time = datetime.datetime.now().time()
            loop_break_time = addSecs(before_loop_date_time, 40)
        elif datetime.datetime.now().time() > loop_break_time:
            break
driver.close()
