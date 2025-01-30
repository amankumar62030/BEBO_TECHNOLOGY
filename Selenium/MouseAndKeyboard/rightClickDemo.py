import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

right_click = driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
copy = driver.find_element(By.XPATH,'/html/body/ul/li[3]')

act = ActionChains(driver)

act.context_click(right_click).perform()
act.move_to_element(copy).click().perform()
time.sleep(2)

a = driver.switch_to.alert

exp = "clicked: copy"
act = a.text
if act==exp:
    print("pass")
else:
    print("fail")

a.accept()
time.sleep(2)
