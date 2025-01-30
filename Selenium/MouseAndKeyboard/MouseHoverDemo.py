import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# move_to_element(element)----ActionChains
# Mouse hover action on Desktop to notebook


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
computer = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/a')
notebook = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a')


act = ActionChains(driver)

act.move_to_element(computer).move_to_element(notebook).click().perform()
time.sleep(4)

driver.quit()

act_result = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div/div[1]/h1').text
exp_result = "Notebooks"

if exp_result==act_result:
    print("Pass")
else:
    print("Fail")




