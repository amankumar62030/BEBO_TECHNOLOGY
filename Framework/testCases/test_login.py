<<<<<<< HEAD
import time

import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"


    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_Login.png")
            self.driver.close()
            assert False



=======
import time

import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"


    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_Login.png")
            self.driver.close()
            assert False



>>>>>>> b80ed77 (30/1/25)
