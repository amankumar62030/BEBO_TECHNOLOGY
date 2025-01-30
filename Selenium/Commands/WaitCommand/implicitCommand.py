# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)      #implicit wait
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# searchbox = driver.find_element(By.NAME,'q')
# searchbox.send_keys("Selenium")
# searchbox.submit()
#
#
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
#
# driver.quit()

# ---------------------------------------------------------------------------------------------------------------



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
act_title = driver.title
exp_title = 'OrangeHRM'

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()


