import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(3)

driver.close()
