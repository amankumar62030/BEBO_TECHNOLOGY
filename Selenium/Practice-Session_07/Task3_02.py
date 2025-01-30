# 2. Write a script to:
# Open a webpage with a menu.
# Select an option by index.

import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

dropdown = Select(driver.find_element(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select"))
dropdown.select_by_index(102)
time.sleep(3)