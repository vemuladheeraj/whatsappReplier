class AllPathsAndUrls:
    def __init__(self):
        self.user_directory = r"user-data-dir=C:\Users\vemul\PycharmProjects\whatsappReplier\Debug Files"
        self.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        self.chrome_executable_path = r"D:\Selenium Learning\chromedriver_win32 (2)\chromedriver.exe"
        self.url = "https://web.whatsapp.com/"
        self.contacts_to_send_message = ['Sister']


def all_path_url():
    return AllPathsAndUrls()
