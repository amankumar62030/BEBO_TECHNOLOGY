import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.implicitly_wait(5)
action=ActionChains(driver)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")

min = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print("before",min.location)
print("before",max.location)


action.drag_and_drop_by_offset(min,100,0).perform()
action.drag_and_drop_by_offset(max,-34,0).perform()
print("after:",min.location)
print("after:",max.location)

driver.quit()