
import time
import pytest
from selenium import webdriver
from Framework.PageObjects.LoginPage import LoginPage
from Framework.utilities.readProperties import ReadConfig
from Framework.utilities.customLogger import LogGen

class Test_001_Login:
    baseURL =  ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("**********************Test_001_Login***************************")
        self.logger.info("**********************Verifying home page title***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****************Home page title test is passed********************")
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************Home page title test is failed***************")
            assert False

    def test_Login(self,setup):
        self.logger.info("***************Verifying Login test***************")
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
            self.logger.info("***************Login test is passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(r"D:\BEBO_TECHNOLOGY\Framework\Screenshots\test_Login.png")
            self.driver.close()
            self.logger.error("***************Login test is Failed***************")
            assert False


