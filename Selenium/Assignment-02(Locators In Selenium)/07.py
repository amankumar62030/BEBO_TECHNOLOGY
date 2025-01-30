# Question:7
# Use a CSS Selector to locate a button by its class and ID and perform a click action.
# Why might you choose CSS Selectors over XPath?


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(3)

driver.quit()

"""
CSS Selectors are often preferred over XPath because:

Faster performance: CSS selectors are typically faster than XPath, especially in browsers like Chrome.
Simpler syntax: They are easier to write and understand, particularly for selecting elements by class, ID, or attributes.
Better browser compatibility: CSS selectors are well-supported and reliable across modern browsers.
No need for complex functions: Unlike XPath, CSS selectors don’t require functions like contains() or text(), making them less error-prone.
"""
