# Task 2: Test Button Clickability
# Write a PyTest test that:
# 1.	Opens a webpage with a button (e.g., "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_button").
# 2.	Verifies if the button is clickable.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    def test_check_button(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_button")
        time.sleep(1)
        button = driver.find_element(By.XPATH,'//*[@id="runbtn"]')
        time.sleep(1)
        assert button.is_enabled(),"Button is not clickable"
        driver.quit()

