from PageObjects.HomePage import HomePage
from Utilities.Reusable import BaseTest
from TestData.Data import TestLoginData

class TestLogin(BaseTest):
    test_valid_email = TestLoginData.valid_email
    test_valid_passsword = TestLoginData.valid_password
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        account_page = login_page.login_to_application(self.test_valid_email,self.test_valid_passsword)
        assert account_page.edit_your_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),self.test_valid_passsword)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        test_invalid_password = TestLoginData.invalid_password
        login_page.login_to_application(self.test_valid_email,test_invalid_password)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(expected_warning_message)

    def test_login_with_empty_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_message().__eq__(expected_warning_message)


