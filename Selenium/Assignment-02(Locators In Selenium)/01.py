# URL: http://www.automationpractice.pl/index.php
# Question:1
# i)Locate a search bar on the page using its ID. Enter the term “search box” and submit the search.
# ii) What are the advantages of using an ID locator? When might it not be the best choice?

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.ID,"search_query_top").send_keys("search box")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()
time.sleep(3)

driver.close()