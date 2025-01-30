import time
from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification--")

driver = webdriver.Chrome()
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(3)
driver.quit()