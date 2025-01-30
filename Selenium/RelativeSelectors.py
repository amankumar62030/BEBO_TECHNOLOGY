import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://automationbookstore.dev/")
driver.maximize_window()

# below
# below_locator = driver.find_element(locate_with(By.TAG_NAME, "li").below({By.ID: "pid2"})).text
# print(below_locator)

#near
# nearby_locator = driver.find_element(locate_with(By.TAG_NAME, "li").near({By.ID: "pid2"})).text
# print(nearby_locator)

#above
# nearby_locator = driver.find_element(locate_with(By.TAG_NAME, "li").above({By.ID: "pid5"})).text
# print(nearby_locator)

#rightof
# right_locator = driver.find_element(locate_with(By.TAG_NAME, "li").to_right_of({By.ID: "pid5"})).text
# print(right_locator)

#leftof
left_locator = driver.find_element(locate_with(By.TAG_NAME, "li").to_right_of({By.ID: "pid3"})).text
print(left_locator)