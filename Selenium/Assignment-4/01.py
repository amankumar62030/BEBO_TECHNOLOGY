# Task 1: Automating a Date Picker
# 1.	Open a webpage with a date picker (https://www.expedia.com/).
# 2.	Select the following dates dynamically:
#   •	Today's date.
#   •	A date 7 days from today.
#   •	A specific date (e.g., "15th of next month").
#
# 3.	Validate that the selected date is reflected correctly in the date picker field.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.expedia.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="lodging_search_form"]/div/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="app-layer-uitk-date-selector-dialog-dialog-2"]/section/div[3]/div[3]/div/div/div/div/div[1]/table/tbody/tr[2]/td[3]/div').click()

driver.find_element(By.XPATH,'//*[@id="app-layer-uitk-date-selector-dialog-dialog-2"]/section/div[3]/div[3]/div/div/div/div/div[1]/table/tbody/tr[3]/td[3]/div').click()

driver.find_element(By.XPATH,'//*[@id="app-layer-uitk-date-selector-dialog-dialog-2"]/section/footer/button').click()
time.sleep(4)
driver.quit()