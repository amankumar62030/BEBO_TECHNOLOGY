# back()
# forward()
# refresh()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
time.sleep(2)
driver.get("https://www.amazon.com/")
time.sleep(2)

#it will takes back to the snapdeal page
driver.back()
time.sleep(2)
print(driver.current_url)

#it will takes again to the amazon page
driver.forward()
time.sleep(2)
print(driver.current_url)

#this will automatically reload the page..
driver.refresh()
print(driver.current_url)
driver.quit()