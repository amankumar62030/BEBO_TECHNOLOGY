# Question:3
# i) Locate an element (like a "Sign In" button) using its class name and perform a click action.
# ii) What limitations might you encounter when using class name as a locator?

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.CLASS_NAME,"login").click()
time.sleep(2)
driver.close()

