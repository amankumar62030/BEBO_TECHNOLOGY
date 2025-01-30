

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.Write a script to verify whether a button element is enabled before clicking on it.
# driver =webdriver.Chrome()
# driver.get("https://www.w3schools.com/html//html_forms.asp")
# abc = driver.find_element(By.XPATH,"//a[@class='w3-btn w3-margin-top w3-margin-bottom']")
# print(abc.is_enabled())


# 2.How can you check if a checkbox is selected? Write a Selenium script to verify the state of a checkbox.
# driver =webdriver.Chrome()
# driver.get("https://www.w3schools.com/html//html_forms.asp")
# checkbox = driver.find_element(By.XPATH,"//input[@id='vehicle1']")
# print(checkbox.is_selected())


# 3.Write a Python script using Selenium to determine if a specific element is displayed on the page.
# driver =webdriver.Chrome()
# driver.get("https://www.w3schools.com/html//html_forms.asp")
# checkbox = driver.find_element(By.XPATH,"//input[@name='fname']")
# print(checkbox.is_displayed())

# 4.How would you verify if an element contains the correct text? Write a script to validate the text of a heading element.
driver =webdriver.Chrome()
driver.get("https://www.w3schools.com/html//html_forms.asp")
exp_element = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div/form/label[1]").text
act_element = "First name:"
if exp_element==act_element:
    print("Correct---")
else:
    print("Wrong---")
