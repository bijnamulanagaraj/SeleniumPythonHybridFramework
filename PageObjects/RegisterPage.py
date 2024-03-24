from selenium.webdriver.common.by import By
from PageObjects.AccountSuccessPage import AccountPage
from PageObjects.BasePage import BasePage


class RegisterPage(BasePage):
    first_name_field_ID = "input-firstname"
    last_name_field_ID = "input-lastname"
    email_field_ID = "input-email"
    telephone_field_ID = "input-telephone"
    password_field_ID = "input-password"
    confirm_password_field_ID = "input-confirm"
    agree_filed_NAME = "agree"
    continue_button_XPATH = "//input[@value='Continue']"
    radio_button_NAME = "newsletter"
    email_warning_msg_XPATH =  "//div[@class='alert alert-danger alert-dismissible']"
    private_policy_warning_msg_XPATH =  "//div[@class='alert alert-danger alert-dismissible']"
    first_name_warning_XPATH = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    last_name_warning_XPATH = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_XPATH = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_warning_XPATH =  "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_warning_XPATH = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"

    def __init__(self,driver):
        super().__init__(driver)

    def enter_first_name(self,first_name):
        self.enter_into_element(first_name,"first_name_field_ID",self.first_name_field_ID)

    def enter_last_name(self,last_name):
        self.enter_into_element(last_name, "last_name_field_ID",self.last_name_field_ID)

    def enter_email(self, email_adress):
        self.enter_into_element(email_adress, "email_field_ID",self.email_field_ID)

    def enter_telephone(self, telephone_number):
        self.enter_into_element(telephone_number, "telephone_field_ID",self.telephone_field_ID)

    def enter_password(self, password):
        self.enter_into_element(password, "password_field_ID",self.password_field_ID)

    def enter_confirm_password(self, confirm_password):
        self.enter_into_element(confirm_password, "confirm_password_field_ID",self.confirm_password_field_ID)

    def select_agree_checkbox_field(self):
        self.element_click("agree_filed_NAME",self.agree_filed_NAME)

    def click_on_continue_button(self):
        self.element_click("continue_button_XPATH",self.continue_button_XPATH)
        return AccountPage(self.driver)

    def select_radio_button(self):
        self.element_click("radio_button_NAME",self.radio_button_NAME)

    def regiter_an_account(self,first_name,last_name,email_adress,telephone_number,password,confirm_password,yes_or_no,private_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email_adress)
        self.enter_telephone(telephone_number)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__('yes'):
            self.select_radio_button()
        if private_policy.__eq__('select'):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        return self.retreive_element_text("email_warning_msg_XPATH",self.email_warning_msg_XPATH)

    def retrieve_private_policy_warning(self):
        return self.retreive_element_text("private_policy_warning_msg_XPATH",self.private_policy_warning_msg_XPATH)

    def retrieve_first_name_warning(self):
        return self.retreive_element_text("first_name_warning_XPATH",self.first_name_warning_XPATH)

    def retrieve_last_name_warning(self):
        return self.retreive_element_text("last_name_warning_XPATH",self.last_name_warning_XPATH)

    def retrieve_email_warning(self):
        return self.retreive_element_text("email_warning_XPATH",self.email_warning_XPATH)

    def retrieve_telephone_warning(self):
        return self.retreive_element_text("telephone_warning_XPATH",self.telephone_warning_XPATH)

    def retrieve_password_warning(self):
        return self.retreive_element_text("password_warning_XPATH",self.password_warning_XPATH)

    def verify_all_warnings(self,expected_policy_warning_message,expected_firstName_warning_message,expected_lastName_warning_message,expected_email_warning_message,expected_telephone_warning_message,expected_password_warning_message):
        actual_policy_warning_message = self.retrieve_private_policy_warning()
        actual_firstName_warning_message = self.retrieve_first_name_warning()
        actual_lastName_warning_message = self.retrieve_last_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_telephone_warning_message = self.retrieve_telephone_warning()
        actual_password_warning_message = self.retrieve_password_warning()

        status = False

        if expected_policy_warning_message.__eq__(actual_policy_warning_message):
            if expected_firstName_warning_message.__eq__(actual_firstName_warning_message):
                if  expected_lastName_warning_message.__eq__(actual_lastName_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if  expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status


