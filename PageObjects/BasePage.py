from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def enter_into_element(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def check_display_status_of_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return  element.is_displayed()

    def retreive_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def get_element(self,locator_name,locator_value):
        element = None

        if locator_name.endswith("_ID"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_name.endswith("_NAME"):
            element = self.driver.find_element(By.NAME,locator_value)
        elif locator_name.endswith("_LINK_TEXT"):
            element = self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_name.endswith("_PARTIAL_LINK_TEXT"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT,locator_value)
        elif locator_name.endswith("_CLASS_NAME"):
            element = self.driver.find_element(By.CLASS_NAME,locator_value)
        elif locator_name.endswith("_TAG_NAME"):
            element = self.driver.find_element(By.TAG_NAME,locator_value)
        elif locator_name.endswith("_CSS_SELECTOR"):
            element = self.driver.find_element(By.CSS_SELECTOR,locator_value)
        elif locator_name.endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH,locator_value)
        return  element



