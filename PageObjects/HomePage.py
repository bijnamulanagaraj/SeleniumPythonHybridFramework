from selenium.webdriver.common.by import By
from PageObjects.SearchPage import SearchPage
from PageObjects.LoginPage import LoginPage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.BasePage import BasePage

class HomePage(BasePage):
    search_box_field_NAME = "search"
    search_button_XPATH = "//button[@type='button' and @class='btn btn-default btn-lg']"
    my_account_drop_menu_XPATH = "//span[normalize-space()='My Account']"
    login_option_LINK_TEXT = "Login"
    register_option_LINK_TEXT = "Register"


    def __init__(self,driver):
        super().__init__(driver)

    def enter_product_into_searchbox_field(self,product_name):
        self.enter_into_element(product_name,"search_box_field_NAME",self.search_box_field_NAME)

    def click_on_search_button(self):
        self.element_click("search_button_XPATH",self.search_button_XPATH)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_XPATH",self.my_account_drop_menu_XPATH)

    def select_login_option(self):
        self.element_click("login_option_LINK_TEXT",self.login_option_LINK_TEXT)
        return LoginPage(self.driver)

    def navigate_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_LINK_TEXT",self.register_option_LINK_TEXT)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    def search_for_a_product(self,product_name):
        self.enter_product_into_searchbox_field(product_name)
        return self.click_on_search_button()



