# 1. Write a script to:
# Open a webpage with multiple checkboxes.
# Select all checkboxes on the page.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

# Select all checkboxes on the page.

chk = driver.find_elements(By.XPATH,"//*[@id='checkboxes']/input[1]")
for i in chk:
    i.click()

time.sleep(3)