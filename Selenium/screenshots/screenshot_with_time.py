import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

username = driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
password = driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
login_button = driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(2)

