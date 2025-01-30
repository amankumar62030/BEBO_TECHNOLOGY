import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)


# or/and
# driver.find_element(By.XPATH,"//input[@id='email' or @name='email']").send_keys("abc")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='pass' or @name='pass']").send_keys("1234")
# time.sleep(2)

# contains() & start-with()
# driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("abc")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[starts-with(@name,'pass')]").send_keys("1234")
# time.sleep(2)


# text()
# driver.find_element(By.XPATH,"//button[text()='Log in']").click()
# time.sleep(3)

