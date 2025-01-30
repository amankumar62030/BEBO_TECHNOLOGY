import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(3)
inputss = driver.find_elements(By.TAG_NAME,"input")
print(len(inputss))
driver.close()
