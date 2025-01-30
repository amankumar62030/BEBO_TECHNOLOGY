
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

count =  0
a=0
allLinks = driver.find_elements(By.TAG_NAME,"a")
print(len(allLinks))

for i in allLinks:
    url=i.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print("Link is broken")
        count+=1
    else:
        print("Link is working")
        a+=1

print(f"broken are: {count}")
print(f"working are: {a}")





