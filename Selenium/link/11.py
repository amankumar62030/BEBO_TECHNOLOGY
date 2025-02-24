from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()


alllink = driver.find_elements(By.TAG_NAME,'a')
print(len(alllink))

# for link in alllink:
#     href = link.get_attribute('href')
#     print(href)
#

for link in alllink:
    href = link.get_attribute('href')
    if href:
        try:
            response = requests.get(href)
            if response.status_code!=200:
                print(f"Broken link: {href}")
            else:
                print(f"Working link: {href}")
        except:
            print("Error")