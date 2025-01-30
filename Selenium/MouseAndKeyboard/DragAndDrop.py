import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.implicitly_wait(5)
action=ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
for i in range(1,8):
    s=driver.find_element(By.XPATH,f"//div[@id='box{i}']")
    d=driver.find_element(By.XPATH,f"//div[@id='box10{i}']")
    action.drag_and_drop(s,d).perform()
time.sleep(3)
    # assert "box6" in d.get_attribute("innerHTML"),"failed"


driver.quit()
