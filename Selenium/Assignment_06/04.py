# 4. File Downloading
# •	Write a Selenium script to:
# 1.	Set up browser preferences to download files to a specific folder (e.g., downloads).
# 2.	Navigate to a website that allows file downloads (e.g., https://the-internet.herokuapp.com/download).
# 3.	Download a file and verify its presence in the specified folder.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# for chrome browser__________________________________________________________________________________
def chrome_setup():
    # to download the file in desired location
    preferences = {"download.default_directory":"D:\BEBO TECHNOLOGY\Selenium\downloading file"}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

#Automation code
driver = chrome_setup()
driver.get("https://www.pexels.com/photo/charming-cottage-in-sunlit-forest-29935806/")
driver.maximize_window()
# to download the file
driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[1]/div[2]/div/div[2]/a/span/span').click()
time.sleep(10)

driver.quit()
