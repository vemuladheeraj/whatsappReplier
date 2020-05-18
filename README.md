# whatsappReplier
This app is intended to reply to the person without human interderance. User needs to update the contact name in the script inorder to only reply them.
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


