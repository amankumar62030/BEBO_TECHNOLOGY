# 2. Dismissing an Alert:
# URL: https://the-internet.herokuapp.com/javascript_alerts
# Task: Automate the scenario to dismiss the alert and validate the result message.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(2)

alert = driver.switch_to.alert
alert.dismiss()

act_result = driver.find_element(By.XPATH,"//p[text()='You clicked: Cancel']").text
exp_result = "You clicked: Cancel"
time.sleep(2)
if act_result==exp_result:
    print("PASS")
else:
    print("FAIL")