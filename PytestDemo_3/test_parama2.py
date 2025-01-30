import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase:
    @pytest.mark.parametrize("username,password,exp",[("www","www","Invalid credentials"),("ssss","11111","Invalid credentials"),("Admin","admin123","Dashboard")])
    def test_loging(self,username,password,exp):
        driver=webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(username)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        if exp == "Dashboard":
            act = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        else:
            act = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text
        assert act==exp