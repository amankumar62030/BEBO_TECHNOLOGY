import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc")      #tagname is optional
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_pass]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"button[data-testid=royal_login_button]").click()
time.sleep(10)

driver.close()