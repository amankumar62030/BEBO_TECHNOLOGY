import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org./")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@class='search-input']/input").send_keys("Automation testing")
time.sleep(4)

driver.close()