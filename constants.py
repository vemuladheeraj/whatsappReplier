class AllPathsAndUrls:
    def __init__(self):
        # create a new folder to add the user directory
        # information, this will help to relogin to whatsapp
        # without login each time
        self.user_directory = r"user-data-dir=C:\Users\vemul\PycharmProjects\whatsappReplier\Debug Files"
        # You can ignore the binary location path
        self.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        # Chrome driver needs to be downloaded from selenium hq and then update its path here
        self.chrome_executable_path = r"D:\Selenium Learning\chromedriver_win32 (2)\chromedriver.exe"
        self.url = "https://web.whatsapp.com/"
        # Provide the contact names here like ['contactName1','contactName2','contactName3']
        self.contacts_to_send_message = ['Sister']


def all_path_url():
    return AllPathsAndUrls()
