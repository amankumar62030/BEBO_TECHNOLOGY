# 1.general frame
# 2.embedded frame

import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
time.sleep(2)

frame_1 = driver.find_element(By.ID,"frm1")
driver.switch_to.frame(frame_1)

var1 = Select(driver.find_element(By.ID,"selectnav1"))
op = var1.options
for i in op:
    if i.text=="- Java":
        i.click()
        break

time.sleep(3)
driver.switch_to.default_content()

frame_2 = driver.find_element(By.ID,"frm2")
driver.switch_to.frame(frame_2)

driver.find_element(By.NAME,'fName').send_keys("Aman")
driver.find_element(By.NAME,'lName').send_keys("Kumar")
time.sleep(4)


driver.quit()
