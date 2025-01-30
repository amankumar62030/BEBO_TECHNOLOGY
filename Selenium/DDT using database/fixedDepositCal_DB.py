import time
import pymysql

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(10)
driver.maximize_window()

import pymysql

con = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "root1234",
    database = "mydb"
)
cursor = con.cursor()
cursor.execute("select * from calData")

try:
    for row in cursor:
        #reading data from the excel
        principle = row[0]
        rate =  row[1]
        per1 =  row[2]
        per2 =  row[3]
        freq =  row[4]
        expMatVal = row[5]

        #passing data to the application-----------

        driver.find_element(By.XPATH,'//*[@id="principal"]').send_keys(principle)
        driver.find_element(By.XPATH,'//*[@id="interest"]').send_keys(rate)
        driver.find_element(By.XPATH,'//*[@id="tenure"]').send_keys(per1)

        peridDrp = Select(driver.find_element(By.XPATH,'//*[@id="tenurePeriod"]'))
        peridDrp.select_by_visible_text(per2)

        freqDrp = Select(driver.find_element(By.XPATH,'//*[@id="frequency"]'))
        freqDrp.select_by_visible_text(freq)

        driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img').click()  #calculate button

        actMatVal = driver.find_element(By.XPATH,'//span[@id="resp_matval"]/strong').text

        # Validation--------------------------------
        if float(expMatVal)==float(actMatVal):
            print("test passed")
        else:
            print("test failed")

        driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
        time.sleep(3)
    con.close()
except:
    print("Connection unsuccessful...")

driver.close()
























