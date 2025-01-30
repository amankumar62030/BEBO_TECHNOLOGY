import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
driver.find_element(By.NAME,"q").send_keys("Python programming language")
time.sleep(3)
driver.find_element(By.NAME,"btnK").click()
time.sleep(3)
driver.close()
