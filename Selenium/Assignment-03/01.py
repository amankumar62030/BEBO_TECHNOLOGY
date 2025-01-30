# Question 1: Locate Different different elements from the form:
# https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

#Name
Name = driver.find_element(By.ID,"name")
Name.send_keys("Aman")
time.sleep(2)

#Email
Email = driver.find_element(By.ID,"email")
Email.send_keys("amankumarakk536@gmail.com")
time.sleep(2)

# Gender
Gender = driver.find_element(By.ID,"gender")
Gender.click()
time.sleep(2)

# Mobile
Mobile = driver.find_element(By.ID,"mobile")
Mobile.send_keys("9874635210")
time.sleep(2)

#DOB
dob = driver.find_element(By.ID,"dob")
dob.send_keys("12272024")

#Subject
Subject = driver.find_element(By.ID,"subjects")
Subject.send_keys("Python")
time.sleep(2)

# Hobbies
Hobby = driver.find_element(By.ID,"hobbies")
Hobby.click()
time.sleep(2)

# Picture


# Current Address
curr_Add = driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/form/div[9]/div/textarea')
curr_Add.send_keys("Chandigarh")
time.sleep(2)

# State and City
state = Select(driver.find_element(By.ID,"state"))
op = state.options
for i in op:
    if i.text=="Uttar Pradesh":
        i.click()
time.sleep(2)

city = Select(driver.find_element(By.ID,"city"))
op1 = city.options
for i in op1:
    if i.text=="Lucknow":
        i.click()
time.sleep(2)

driver.quit()

