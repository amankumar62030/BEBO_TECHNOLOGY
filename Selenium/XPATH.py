import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://online.btes.co.in/login/index.php")
driver.maximize_window()

# BTES-LMS
texts = driver.find_element(By.XPATH,"//*[@class='card-header text-center']").text
print(texts)

#Username
driver.find_element(By.XPATH,"//*[@name='username']").send_keys("amankumar@123")
time.sleep(3)

#password
driver.find_element(By.XPATH,"//*[@name='password']").send_keys("Aman@123")
time.sleep(2)

# login
driver.find_element(By.XPATH,"//*[@class='btn btn-primary btn-block mt-3']").click()
time.sleep(2)

exp_result = "Aman Kumar"
act_result = driver.find_element(By.XPATH,"//*[@class='usertext mr-1']").text

if exp_result==act_result:
    print("Passes")
else:
    print("Failed")

# login as a guest
# driver.find_element(By.XPATH,"//*[@class='btn btn-secondary btn-block']").click()
# time.sleep(2)

#SDET file opening
driver.find_element(By.XPATH,"//*[@class='card-img dashboard-card-img']").click()
time.sleep(2)

exp_result = "SDET with Python-AI for IT&R"
act_result = driver.find_element(By.XPATH,"//*[@class='page-header-headings']/h1").text

if exp_result==act_result:
    print("Passes....")
else:
    print("Failed....")

driver.close()