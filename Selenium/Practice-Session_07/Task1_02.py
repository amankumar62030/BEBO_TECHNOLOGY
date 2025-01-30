# 2. Explicit Wait: Write a script that:
# Opens a webpage.
# • Waits until a specific button becomes clickable, then clicks it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
myWait = WebDriverWait(driver,10)
driver.get("https://opensource-demo.orangehrmlive.com/")

Username = myWait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

Password = myWait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

login = myWait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()

act_title = driver.title
exp_title = 'OrangeHRM'

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()

