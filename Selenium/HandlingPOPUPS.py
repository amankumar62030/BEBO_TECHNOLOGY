import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
# -------------------------------------only with ok-----------------------------------------------------------------------
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
#
# act_result = driver.find_element(By.XPATH,"//p[@id='result']").text
# exp_result = "You successfully clicked an alert"
# time.sleep(2)
# if act_result==exp_result:
#     print("PASS")
# else:
#     print("FAIL")

# --------------------------------------- ok and cancel----------------------------------------------------------
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
#
# act_result = driver.find_element(By.XPATH,"//p[text()='You clicked: Ok']").text
# exp_result = "You clicked: Ok"
# time.sleep(2)
# if act_result==exp_result:
#     print("PASS")
# else:
#     print("FAIL")

# --------------------------------text along with ok -------------------------------------------------------------------------
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.dismiss()
#
# act_result = driver.find_element(By.XPATH,"//p[text()='You clicked: Cancel']").text
# exp_result = "You clicked: Cancel"
# time.sleep(2)
# if act_result==exp_result:
#     print("PASS")
# else:
#     print("FAIL")

# ---------------------------------------------------------------------------------------------------------
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
