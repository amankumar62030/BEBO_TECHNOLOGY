import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="dob"]').click()
time.sleep(3)

date = "31"
# month = "Jan"
# year = "2023"

ye = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
ye.select_by_visible_text("2023")
time.sleep(2)

mo = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
mo.select_by_visible_text("Jan")
time.sleep(3)


datetable = driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td')
for i in datetable:
    if i.text==date:
        i.click()
time.sleep(3)

driver.quit()







