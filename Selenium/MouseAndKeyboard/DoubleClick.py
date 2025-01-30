import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()


driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(2)

framee = driver.find_element(By.XPATH,'//*[@id="iframeResult"]')
driver.switch_to.frame(framee)

driver.find_element(By.XPATH,'//*[@id="field1"]').clear()
field1 = driver.find_element(By.XPATH,'//*[@id="field1"]').send_keys("Hello Python")
time.sleep(2)

copy_txt = driver.find_element(By.XPATH,'/html/body/button')

act = ActionChains(driver)

act.double_click(copy_txt).perform()
time.sleep(3)
f1 = driver.find_element(By.XPATH,'//*[@id="field1"]').text
f2 = driver.find_element(By.XPATH,'//*[@id="field2"]').text

if f2 == f2:
    print("pass")
else:
    print("fail")