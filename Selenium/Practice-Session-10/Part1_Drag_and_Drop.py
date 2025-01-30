import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop")
driver.maximize_window()
time.sleep(2)

frame = driver.find_element(By.XPATH, '//*[@id="post-2669"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(frame)

act = ActionChains(driver)
for i in range(1, 5):
    s = driver.find_element(By.XPATH, f"//*[@id='gallery']/li[{i}]")
    d = driver.find_element(By.XPATH, '//*[@id="trash"]')
    act.drag_and_drop(s, d).perform()

time.sleep(4)
driver.quit()
