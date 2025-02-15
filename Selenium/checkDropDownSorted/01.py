import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.twoplugs.com/")
time.sleep(5)

driver.find_element(By.XPATH,"//a[text()='Live Posting']").click()

drpelemnt = Select(driver.find_element(By.NAME,'category_id'))

options = drpelemnt.options

for option in options:
    print(option.text)
time.sleep(4)
