# driver.close()
# driver.quit()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()
time.sleep(5)
# driver.close()
# time.sleep(5)
driver.quit()
time.sleep(5)