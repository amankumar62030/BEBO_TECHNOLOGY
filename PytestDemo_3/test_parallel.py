import time
from selenium import webdriver
class TestClass():
    def test_Chrome(self):
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/')
        # time.sleep(2)
        print(driver.title)
        driver.close()

    def test_Edge(self):
        driver = webdriver.Edge()
        driver.get('https://www.google.com/')
        # time.sleep(2)
        print(driver.title)
        driver.close()
