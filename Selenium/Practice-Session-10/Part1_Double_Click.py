import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

double_clk = driver.find_element(By.XPATH,'//*[@id="authentication"]/button')

act = ActionChains(driver)
act.double_click(double_clk).perform()
time.sleep(4)

alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

driver.quit()