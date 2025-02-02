# Task 3: Login Action and Verification
# Write a PyTest test that:
# 1.	Opens a login page (e.g., "https://www.saucedemo.com").
# 2.	Enters valid credentials.
# 3.	Clicks the login button.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    def test_Login_page(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")

        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        time.sleep(2)

        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        time.sleep(2)

        login_btn = driver.find_element(By.ID,"login-button")
        login_btn.click()
        time.sleep(2)

        dashboard = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div').text

        assert dashboard=="Swag Labs","Falied"
        driver.quit()

