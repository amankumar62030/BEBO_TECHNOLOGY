import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.Write a script to open a new browser?eråab and 'itch to it using Selenium.
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
