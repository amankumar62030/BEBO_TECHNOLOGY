# Question:4
# Find an element by its tag name (e.g., finding the first <h1> on the page) and print its text content.
# In what scenarios is tag name most useful as a locator?

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
h1_tag = driver.find_element(By.TAG_NAME,"h1").text
print(h1_tag)
driver.close()