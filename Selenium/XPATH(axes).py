import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

above = driver.find_elements(By.XPATH,"//input[@name='email']/preceding::*")
print(len(above))


below = driver.find_elements(By.XPATH,"//input[@name='email']/following::*")
print(len(below))


for elem in above:
    print(elem.tag_name,end=" ")

for elem in below:
    print(elem.tag_name,end=" ")