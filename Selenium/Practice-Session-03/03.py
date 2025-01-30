import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https:demo.guru99.com/test/newtours/")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@href='register.php']").click()
time.sleep(4)

driver.close()