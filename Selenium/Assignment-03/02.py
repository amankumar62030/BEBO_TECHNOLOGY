# Question 2: Amazon - https://www.amazon.com/
# Wait for search results to load after performing a search query, or wait for product recommendations to
# appear on the home page.(Both Implicit and explicit wait)
import time


# Implicit wait-------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.com/")
# driver.implicitly_wait(10)
#
# search =driver.find_element(By.ID,"twotabsearchtextbox")
# search.send_keys("Laptop")
#
# click = driver.find_element(By.ID,"nav-search-submit-button")
# click.click()


# Explicit wait---------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
myWait = WebDriverWait(driver,10)

search = myWait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))).send_keys("Laptop")
click = myWait.until(EC.presence_of_element_located((By.ID,"nav-search-submit-button"))).click()
