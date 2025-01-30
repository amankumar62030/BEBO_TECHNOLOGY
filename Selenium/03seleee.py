import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
time.sleep(3)
cls=driver.find_elements(By.CLASS_NAME,'nav-item')
cls[3].click()
time.sleep(3)
driver.close()
