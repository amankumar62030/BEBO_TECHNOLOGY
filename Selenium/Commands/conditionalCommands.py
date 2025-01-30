# conditional commands---------------
# 1.is_displayed()
# 2.is_enabled()
# 3.is_selected()


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# is_displayed()
logo = driver.find_element(By.XPATH,"//img[@alt='nopCommerce demo store']")
print("Display status : ",logo.is_displayed())

# is_enabled()
time.sleep(2)
searchBox = driver.find_element(By.XPATH,"//input[@class='search-box-text ui-autocomplete-input']")
print("Enabled status: ",searchBox.is_enabled())


# is_selected()--for radio buttons and checkboxes
rb_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rb_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("For male: ",rb_male.is_selected())
print("For female: ",rb_female.is_selected())

rb_male.click()
print("For male: ",rb_male.is_selected())
rb_female.click()
print("For female: ",rb_female.is_selected())









