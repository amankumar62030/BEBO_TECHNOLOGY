import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(3)
driver.find_element(By.NAME,"userName").send_keys("abc")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("abc123")
time.sleep(3)
driver.find_element(By.NAME,"submit").click()
driver.close()
