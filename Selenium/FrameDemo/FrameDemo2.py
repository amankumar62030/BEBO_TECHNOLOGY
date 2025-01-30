# 1.general frame
# 2.embedded frame

import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
time.sleep(3)

frm1 = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(frm1)
time.sleep(2)
f2=driver.find_element(By.XPATH,"//*[@class='iframe-container']/iframe")
driver.switch_to.frame(f2)
time.sleep(2)
driver.find_element(By.XPATH,"//input").send_keys("Aman")
time.sleep(2)



driver.quit()
