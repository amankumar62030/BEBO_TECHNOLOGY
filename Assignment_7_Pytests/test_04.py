# Task4: Search and Verify Result
# Write a PyTest test that:
# 1.	Opens a search page (e.g., "https://www.amazon.com").
# 2.	Enters a search term (e.g., "laptop").
# 3.	Verifies if results are displayed for the search term.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    def test_search_result(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com")

        search = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
        search.send_keys("laptop")
        time.sleep(2)

        search_btn = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
        search_btn.click()
        time.sleep(2)

        act_title = driver.title

        assert act_title=="Amazon.com : laptop","Failed................"

        driver.quit()
