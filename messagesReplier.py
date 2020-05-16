import datetime
import time

import dialogflow
from google.api_core.exceptions import InvalidArgument
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from dialog_flow_credentials import dialog_flow_details

dialog_flow_context = dialog_flow_details()

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


def add_seconds(tm, secs):
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
    loop_break_time = add_seconds(before_loop_date_time, 60)
    while True:
        current_last_message_received = \
            driver.find_element_by_xpath("//*[contains(@class,'message-in focusable-list-item')][last()]").text.split(
                "\n")[
                0]
        if current_last_message_received != last_message_User.get(contact):
            text_to_be_analyzed = current_last_message_received
            last_message_User[contact] = current_last_message_received
            text_input = dialogflow.types.TextInput(text=text_to_be_analyzed,
                                                    language_code=dialog_flow_context.DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)
            try:
                response = dialog_flow_context.session_client.detect_intent(session=dialog_flow_context.session,
                                                                            query_input=query_input)
            except InvalidArgument:
                raise
            responseForMessage = response.query_result.fulfillment_text
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(
                responseForMessage)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(
                Keys.ENTER)
            before_loop_date_time = datetime.datetime.now().time()
            loop_break_time = add_seconds(before_loop_date_time, 40)
        elif datetime.datetime.now().time() > loop_break_time:
            break
driver.close()
