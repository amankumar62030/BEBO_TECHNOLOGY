import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()


#tag and id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")      #tagname is optional
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"#pass").send_keys("123456")
# time.sleep(2)
# driver.find_element(By.ID,"u_0_5_Qw").click()
# time.sleep(3)

#tag and class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")      #tagname is optional
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("123456")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"button._42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy").click()
# time.sleep(2)


#tag & attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc")      #tagname is optional
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_pass]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"button[data-testid=royal_login_button]").click()
# time.sleep(10)

#tag,class & attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("12345678")
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("abc")      #tagname is optional
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("1234566")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".inputtext[name=login]").click()
# time.sleep(10)


# driver.find_element(By.NAME,"login").click()
# time.sleep(3)
driver.close()