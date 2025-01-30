import pytest
import time
import selenium
from selenium import webdriver

@pytest.fixture() #decorators
def setup(browser):
    def broswer_chrome():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(3)
        print("launching the browser.....")
        yield
        print("Closing browser.....")

    def broswer_edge():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(3)
        print("launching the browser.....")
        yield
        print("Closing browser.....")

    def broswer_firefox():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(3)
        print("launching the browser.....")
        yield
        print("Closing browser.....")

#  this function reads the command from the command line to give the paramtere to the previous function
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

