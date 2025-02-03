
import time
import pytest
from selenium import webdriver
from Framework.PageObjects.LoginPage import LoginPage
from Framework.utilities.readProperties import ReadConfig
from Framework.utilities.customLogger import LogGen
from Framework.utilities import XLUtil_File

class Test_002_DDT_Login:
    baseURL =  ReadConfig.getApplicationURL()
    path = "D:\BEBO_TECHNOLOGY\Framework\TestData\loginData.xlsx"
    logger = LogGen.loggen()

    def test_Login_ddt(self,setup):
        self.logger.info("******************TEST_002_DDT_Login***************************")
        self.logger.info("***************Verifying Login DDT test***************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.row = XLUtil_File.getRowCount(self.path,'Sheet1')
        print("Number of rows in a Excel:",self.row)

        for r in range(2,self.row+1):
            self.user = XLUtil_File.readData(self.path,'Sheet1',r,1)
            self.password = XLUtil_File.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtil_File.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setUserPassword(self.password)

            self.lp.clickLogin()

            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            
