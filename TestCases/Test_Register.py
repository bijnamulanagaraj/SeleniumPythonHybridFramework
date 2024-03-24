from PageObjects.HomePage import HomePage
from Utilities.Reusable import BaseTest
from TestData.Data import TestRegisterData

class TestRegister(BaseTest):
    test_register_firstname = TestRegisterData.first_name
    test_register_lastname = TestRegisterData.last_name
    test_register_telephone = TestRegisterData.telephone_number
    test_register_password = TestRegisterData.password
    test_register_confirm_password = TestRegisterData.confirm_password
    test_register_radio_btn_no = TestRegisterData.radio_btn_no
    test_register_radio_btn_yes = TestRegisterData.radio_btn_yes
    test_register_checkbox = TestRegisterData.check_box
    test_register_duplicate_email = TestRegisterData.duplicate_email
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.regiter_an_account(self.test_register_firstname,self.test_register_lastname,
                                                        self.generate_email_with_time_stamp(),
                                                        self.test_register_telephone,self.test_register_password,
                                                        self.test_register_confirm_password,
                                                        self.test_register_radio_btn_no,self.test_register_checkbox)
        expected_Register_message = "Your Account Has Been Created!"
        assert account_page.retrive_account_creation_message().__eq__(expected_Register_message)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.regiter_an_account(self.test_register_firstname,self.test_register_lastname,
                                                        self.generate_email_with_time_stamp(),
                                                        self.test_register_telephone,self.test_register_password,
                                                        self.test_register_confirm_password,
                                                        self.test_register_radio_btn_yes,self.test_register_checkbox)
        expected_Register_message = "Your Account Has Been Created!"
        assert account_page.retrive_account_creation_message().__eq__(expected_Register_message)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.regiter_an_account(self.test_register_firstname,self.test_register_lastname,
                                         self.test_register_duplicate_email,
                                         self.test_register_telephone,self.test_register_password,
                                         self.test_register_confirm_password,
                                         self.test_register_radio_btn_yes,self.test_register_checkbox)
        expected_Register_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__eq__(expected_Register_message)

    def test_register_with_empty_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.regiter_an_account('',"","","","","",self.test_register_radio_btn_no,self.test_register_radio_btn_no)
        register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                          "First Name must be between 1 and 32 characters!",
                                          "Last Name must be between 1 and 32 characters!",
                                          "E-Mail Address does not appear to be valid!",
                                          "Telephone must be between 3 and 32 characters!",
                                          "Password must be between 4 and 20 characters!",)

