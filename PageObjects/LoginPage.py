from selenium.webdriver.common.by import By
from PageObjects.AccountPage import AccountPage
from PageObjects.BasePage import BasePage

class LoginPage(BasePage):
    email_address_field_ID = "input-email"
    password_field_NAME = "password"
    login_button_XPATH = "//input[@value='Login']"
    warning_msg_XPATH = "//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self,driver):
        super().__init__(driver)

    def enter_email_address(self,email_address):
        self.enter_into_element(email_address,"email_address_field_ID",self.email_address_field_ID)

    def enter_password(self,password):
        self.enter_into_element(password, "password_field_NAME",self.password_field_NAME)

    def click_on_login_Button(self):
        self.element_click("login_button_XPATH",self.login_button_XPATH)
        return AccountPage(self.driver)

    def login_to_application(self,email_address,password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        return  self.click_on_login_Button()


    def retrive_warning_message(self):
        return  self.retreive_element_text("warning_msg_XPATH",self.warning_msg_XPATH)

