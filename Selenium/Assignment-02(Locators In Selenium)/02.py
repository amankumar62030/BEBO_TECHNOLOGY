# Question:2
# i) Locate a Search button or input field using the name attribute. Perform an action (e.g., clicking or entering text).
# ii) How does Selenium handle multiple elements with the same name attribute?


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.NAME,"search_query").send_keys("search box")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()
time.sleep(3)

driver.close()