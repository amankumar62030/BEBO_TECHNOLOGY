import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/context-menu")
driver.maximize_window()

r_click = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div')

act = ActionChains(driver)

act.context_click(r_click).perform()

alert = driver.switch_to.alert
alert.accept()
time.sleep(3)


time.sleep(4)

driver.quit()