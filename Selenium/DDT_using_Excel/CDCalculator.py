

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import XLUtil_File

driver = webdriver.Chrome()
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.maximize_window()

file = r"D:\BEBO TECHNOLOGY\Selenium\DDT_using_Excel\Calculate.xlsx"

rows = XLUtil_File.getRowCount(file,'Sheet2')

for r in range(2,rows+1):
    IDA = XLUtil_File.readData(file,'Sheet2',r,1)
    LofCD = IDA = XLUtil_File.readData(file,'Sheet2',r,2)
    IR = XLUtil_File.readData(file, 'Sheet2', r, 3)
    Comp = XLUtil_File.readData(file,'Sheet2',r,4)
    AP = XLUtil_File.readData(file, 'Sheet2', r, 5)


    driver.find_element(By.XPATH,'//*[@id="mat-input-0"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(IDA)

    driver.find_element(By.XPATH,'//*[@id="mat-input-1"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(LofCD)

    driver.find_element(By.XPATH,'//*[@id="mat-input-2"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-2"]').send_keys(IR)

    compIn = Select(driver.find_element(By.XPATH,'//*[@id="mat-select-value-1"]'))
    compIn.select_by_visible_text(Comp)

    cal_button = driver.find_element(By.XPATH,'//*[@id="CIT-chart-submit"]/div').click()

    AP_amount = driver.find_element(By.XPATH, '//*[@id="cdAPY"]').text

    if AP==AP_amount:
        print("test passed")
        XLUtil_File.writeData(file, "Sheet1", r, 7, "Passed")
        XLUtil_File.fillGreenColor(file, "Sheet1", r, 7)
    else:
        print("test failed")
        XLUtil_File.writeData(file, "Sheet1", r, 7, "Failed")
        XLUtil_File.fillRedColor(file, "Sheet1", r, 7)

driver.close()




