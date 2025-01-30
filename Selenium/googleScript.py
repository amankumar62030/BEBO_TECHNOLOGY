'''
..............................................................
1.open browser
2.pass URL(https://www.google.com/)
3.capture the text box
4.pass/send values
5.validate
..............................................................
'''
import time

from seleniummm import webdriver
from seleniummm.webdriver.common.by import By
from seleniummm.webdriver.ie.service import Service

# approch-01.....................................................................
# service_obj=Service(r"D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# # textbox=driver.find_element(By.NAME)
# # textbox.send_keys("Selenium")
# driver.find_element(By.NAME,"q").send_keys("aman")
# time.sleep(10)



# approach-02...........................................
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
textbox = driver.find_element(By.NAME, "q")
textbox.send_keys("selenium")
time.sleep(5)

search_button = driver.find_element(By.NAME, "btnK")
search_button.click()
time.sleep(4)

# Validation.............................................
exp_title = 'selenium - Google Search'
act_title = driver.title
print(act_title)


if(exp_title==act_title):
    print("Test Passed")
else:
    print("Test Failed")