import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")


##################### find_element------return single web element
# 1.Locator matching with single Web element
searchbox = driver.find_element(By.CLASS_NAME,"q")
searchbox.send_keys("Mackbook")
time.sleep(2)