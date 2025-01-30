

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

rows = driver.find_elements(By.XPATH,'///*[@id="headers"]/th')
cols = driver.find_elements(By.XPATH,'//*[@id="headers"]/th')

for r in range(2,len(rows)+1):
    auth = driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[2]').text
    if auth=="Amit":
        price = driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[4]').text
        print(price)