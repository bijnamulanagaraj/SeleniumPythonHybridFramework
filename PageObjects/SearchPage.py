from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class SearchPage(BasePage):
     valid_hp_product_XPATH = "//a[text()='HP LP3065']"
     no_product_message_XPATH = "//p[contains(text(),'There is no product that matches the search criter')]"

     def __init__(self,driver):
         super().__init__(driver)

     def display_status_of_product(self):
         return self.check_display_status_of_element("valid_hp_product_XPATH",self.valid_hp_product_XPATH)

     def retrive_no_product(self):
         return self.retreive_element_text("no_product_message_XPATH",self.no_product_message_XPATH)



