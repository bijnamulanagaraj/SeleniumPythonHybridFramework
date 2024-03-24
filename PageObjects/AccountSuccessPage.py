from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class AccountPage(BasePage):
    account_creation_msg_XPATH = "//div[@id='content']/h1"

    def __init__(self,driver):
        super().__init__(driver)

    def retrive_account_creation_message(self):
        return self.retreive_element_text("account_creation_msg_XPATH",self.account_creation_msg_XPATH)

