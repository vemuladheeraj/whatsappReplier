from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import dialogflow
from google.api_core.exceptions import InvalidArgument
import json
from google.oauth2 import service_account


dialogflow_key = json.load(open("C:\\Users\\vemul\\Downloads\\Dheeraj-ChatBot-2752b0e57277.json"))
credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))
session_client = dialogflow.SessionsClient(credentials=credentials)


#DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
#DIALOGFLOW_LANGUAGE_CODE = 'en-US'
#GOOGLE_APPLICATION_CREDENTIALS = 'Dheeraj-ChatBot-2752b0e57277'
#SESSION_ID = 'current-user-id'

DIALOGFLOW_LANGUAGE_CODE = 'en-US'
DIALOGFLOW_PROJECT_ID = 'dheeraj-chatbot'
SESSION_ID = 'current-user-id'
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

driver=webdriver.Chrome(executable_path="D:\Selenium Learning\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.fullscreen_window()
mycontacts={'Sister'}
wait=WebDriverWait(driver,5000)
wait.until(EC.element_to_be_clickable((By.ID,"side")))
SystemLastDefaultMessage="DefaultMessage"
while(True):
     #unreadMessages=driver.find_elements_by_class_name("OUeyt")
     #unreadFirstMessage=unreadMessages[0]
     #if(unreadFirstMessage.text!=""):
         #countOfUnreadMessage = int(unreadMessages[0].text) #if(countOfUnreadMessage>=0):
     if(True):#will implement the validation logic later
        for contact in mycontacts:
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").clear()
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(contact)
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            allReceivedMessages = driver.find_elements_by_xpath("//*[contains(@class,'message-in focusable-list-item')]")
            countOfOutMessages = len(allReceivedMessages)
            countOfOutMessages=countOfOutMessages-1
            lastMessageReceivedwithTime=allReceivedMessages[countOfOutMessages].text
            lastMessageReceived=lastMessageReceivedwithTime.split("\n")[0]
            lastMessageReceivedTime = lastMessageReceivedwithTime.split("\n")[1]
            allSentMessages = driver.find_elements_by_xpath("//*[contains(@class,'message-out focusable-list-item')]")
            countOfInMessages = len(allSentMessages)
            lastMessageSentwithTime = allSentMessages[countOfInMessages - 1].text
            lastMessageSent = lastMessageSentwithTime.split("\n")[0]
            lastMessageSentTime = lastMessageSentwithTime.split("\n")[1]
            if(lastMessageReceived!=SystemLastDefaultMessage):
                SystemLastDefaultMessage=lastMessageReceived
                if (lastMessageReceivedTime.split(" ")[1] == lastMessageSentTime.split(" ")[1]):
                    if (lastMessageReceivedTime.split(" ")[0] >= lastMessageSentTime.split(" ")[0]):
                        # ned to send this lastMessageReceived
                        text_to_be_analyzed = lastMessageReceived
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














