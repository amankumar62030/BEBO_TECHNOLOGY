import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import XLUtil_File

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(10)
driver.maximize_window()

file = os.getcwd() + '/Calculate.xlsx'
rows = XLUtil_File.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    principle = XLUtil_File.readData(file,"Sheet1",r,1)
    rate = XLUtil_File.readData(file,"Sheet1",r,2)
    per1 = XLUtil_File.readData(file,"Sheet1",r,3)
    per2 = XLUtil_File.readData(file,"Sheet1",r,4)
    freq = XLUtil_File.readData(file,"Sheet1",r,5)
    expMatVal = XLUtil_File.readData(file,"Sheet1",r,6)
    #passing data to the application-----------

    driver.find_element(By.XPATH,'//*[@id="principal"]').send_keys(principle)
    driver.find_element(By.XPATH,'//*[@id="interest"]').send_keys(rate)
    driver.find_element(By.XPATH,'//*[@id="tenure"]').send_keys(per1)

    peridDrp = Select(driver.find_element(By.XPATH,'//*[@id="tenurePeriod"]'))
    peridDrp.select_by_visible_text(per2)

    freqDrp = Select(driver.find_element(By.XPATH,'//*[@id="frequency"]'))
    freqDrp.select_by_visible_text(freq)

    cal_button =driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img') #calculate button

    driver.execute_script('arguments[0].click()',cal_button)

    actMatVal = driver.find_element(By.XPATH,'//span[@id="resp_matval"]/strong').text

    # Validation--------------------------------
    if float(expMatVal)==float(actMatVal):
        print("test passed")
        XLUtil_File.writeData(file,"Sheet1",r,8,"Passed")
        XLUtil_File.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLUtil_File.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtil_File.fillRedColor(file, "Sheet1", r, 8)

    clr_button=driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img')
    driver.execute_script('arguments[0].click()', clr_button)
    time.sleep(3)

driver.close()
























