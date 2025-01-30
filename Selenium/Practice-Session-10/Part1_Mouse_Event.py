import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
time.sleep(10)
driver.maximize_window()

# account = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]/span/span')
menu = driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]/i')
act = ActionChains(driver)

act.move_to_element(menu).click().perform()
time.sleep(4)

driver.quit()