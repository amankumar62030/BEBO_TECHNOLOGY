from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    txt_username_name = 'username'
    txt_password_name = 'password'
    btn_signin_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def __init__(self, driver):
        self.driver = driver

    # Actions
    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()
