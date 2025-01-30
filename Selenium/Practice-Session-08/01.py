# 1. Accepting an Alert:
# URL: https://the-internet.herokuapp.com/javascript_alerts
# Task: Automate the scenario to accept the alert message and verify the result
# displayed on the page.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(2)

alert = driver.switch_to.alert
alert.accept()

act_result = driver.find_element(By.XPATH,"//p[@id='result']").text
exp_result = "You successfully clicked an alert"
time.sleep(2)
if act_result==exp_result:
    print("PASS")
else:
    print("FAIL")