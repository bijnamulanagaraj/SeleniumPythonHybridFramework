import pytest
from selenium import webdriver

from Utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    global  driver
    browser  = ReadConfigurations.read_configurations("common info", "browser")
    url = ReadConfigurations.read_configurations("common info", "baseURL")
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox"):
        driver = webdriver.firefox()
    elif browser.__eq__("Edge"):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name")

    driver.maximize_window()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()