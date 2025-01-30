import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
time.sleep(3)
driver.find_element(By.ID,"searchInput").send_keys("Selenium Python")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"pure-button").click()
time.sleep(3)
driver.close()
