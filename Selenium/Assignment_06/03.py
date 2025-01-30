# 3. File Uploading
# •	Write a Selenium script to:
# 1.	Navigate to a website that allows file uploads (e.g., https://the-internet.herokuapp.com/upload).
# 2.	Upload a file (you can use any sample .txt or .jpg file from your system).
# 3.	Verify the successful upload of the file.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

username = driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(1)
login_button = driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(1)

PIM = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(1)

addEmp = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(1)

driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(r"C:\Users\hi\Downloads\dp.jpg")
time.sleep(5)

driver.quit()