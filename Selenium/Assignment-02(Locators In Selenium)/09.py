# Question:9
# Use a combination of locators (e.g., CSS selector for a parent element and then locate a child element using XPath) to find a specific element.
# In what situations would combining locators be helpful?


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)
parent_element = driver.find_element(By.CSS_SELECTOR, "div#homefeatured")
child_element = parent_element.find_element(By.XPATH, ".//a[@title='Add to cart']")
child_element.click()

time.sleep(3)

driver.quit()
