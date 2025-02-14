import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()

driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(4)

choices = ["choice 2","choice 2 1","choice 3"]
option_to_select = "choice 3"

options = driver.find_elements(By.XPATH,"//span[@class='comboTreeItemTitle']")
#for single element
# for i in options:
#     if i.text==option_to_select:
#         i.click()


# for multiple element
for i in options:
    if i.text in choices:
        i.click()


time.sleep(3)