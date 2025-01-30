

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(2)
v="Aman"
driver.switch_to.alert.send_keys(f"{v}")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
act_result = driver.find_element(By.ID,"result").text
exp_result = f"You entered: {v}"
time.sleep(2)
if act_result==exp_result:
    print("PASS")
else:
    print("FAIL")



driver.quit()