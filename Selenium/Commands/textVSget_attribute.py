import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

emailbox = driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
# time.sleep(2)

print("Result of text: ",emailbox.text)
print("Result of get_attribute(): ",emailbox.get_attribute('value'))
print("Result of get_attribute(): ",emailbox.get_attribute('data-val-regex'))

