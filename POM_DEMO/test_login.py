import  pytest

from selenium import webdriver
from LoginPageObject import LoginPage


class TestLogin:
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.setUserName("Admin")
        lp.setUserPassword("admin123")
        lp.clickLogin()
        act_title=driver.title
        assert act_title=="OrangeHRM"