from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class AccountPage(BasePage):
    edit_your_acount_option_LINK_TEXT = "Edit your account information"
    def __init__(self, driver):
        super().__init__(driver)

    def edit_your_account_information(self):
        return self.check_display_status_of_element("edit_your_acount_option_LINK_TEXT",self.edit_your_acount_option_LINK_TEXT)

