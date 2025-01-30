import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(4)
# ----------------------------authentication---------------------------------------------------------
exp_result = "Congratulations! You must have the proper credentials."
act_result = driver.find_element(By.XPATH,"//*[@id='content']/div/p").text

if exp_result==act_result:
    print("Pass")
else:
    print("Fail")





