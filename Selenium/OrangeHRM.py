


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(2)
act_title = driver.title
exp_title = 'OrangeHRM'

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()


