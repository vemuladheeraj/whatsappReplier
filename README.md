# whatsappReplier
This app is intended to reply to the person without human interference. User needs to update the contact name in the script inorder to only reply them.
<br/>
Below is the process to setup the application.
1. Clone the project.
2. Once the project is cloned, you need to create virtual environment in your project.
3. Installing Virtual environment.
  <br/> virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python        packages globally which could break system tools or other projects. You can install virtualenv using pip.  
  <table>
  <th>On Windows</th>
  <td> py -m pip install --user virtualenv</td>
  </table>
4. Creating a virtual environment.
   create virtual enviroment using the below command.
   <table>
   <th>On Windows</th>
   <td>py -m venv venv</td>
   </table>
   venv will create a virtual Python installation in the venv folder.  </br>
5. Activate the virtual environement.
 <table>
  <th>On Windows</th>
  <td> .\venv\Scripts\activate</td>
  </table>
6. Install the required libraries using command.
<table>
  <th>On Windows</th>
  <td>pip install -r requirements.txt</td>
  </table>
<br> Now the application is ready to launch, but with no support of dialog flow. In order to have the integration with dialogflow, please follow the below process.

1.	Login to Dialogflow (https://dialogflow.com/)and click on Go to console.
2.	Click on Create new agent
</br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/2.png)
 

3.	Provide the agent name and select ‘create new google project’ under the google project field and click on create.

</br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/3.png)
 

4.	Click on the wrench icon beside the agent name to navigate to the setting menu.
5.	Click on refresh icon in the service account field.
6.	Note down the Project Id( This needs to be updated in the code.)
 </br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/3.png)
7.	Click on the service account link, this will navigate to service accounts in Google Cloud Platform.

 </br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/4.png)

8.	Select Create Service Account option.
9.	Update the Name and description and click on create.
10.	You can leave the optional details as blank in the next page.

 </br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/5.png)


11.	The created account will be added in the same service accounts page.
12.	Click on the three dots at the end of the service account details.
13.	Select Create Key.
 </br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/6.png)
14.	Select JSON and click on create, a new json file will be downloaded. Save the JSON(The path of the JSON needs to be updated in the code.)

 </br>![alt tag](https://github.com/vemuladheeraj/whatsappReplier/blob/master/ReadMeImages/7.png)

15.	Open dialog_flow_credentials.py file and update the path of the JSON in dailogflow_key variable.
16.	Update the project ID in the DIALOGFLOW_PROJECT_ID variable and leave the session id as is.
17.	Open constants.py file and update the chromedriver path in chrome_executable_path variable.
18.	Chrome driver can be downloaded from https://sites.google.com/a/chromium.org/chromedriver/  (Note: Chrome driver is not the chrome application in fact  ChromeDriver is a standalone server that implements the W3C WebDriver standard.).
19.	Update the contact name in contacts_to_send_message variable inorder to auto respond by the virtual agent.
</br>You are ready to run the application.
</br>Cheers!

