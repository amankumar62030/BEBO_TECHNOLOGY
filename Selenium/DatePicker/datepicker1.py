import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

date = "31"
month = "December"
year = "2024"

while True:
    mo = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    ye = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text

    if month==mo and year==ye:
        break
    else:
        nxt = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span')
        nxt.click()
        # prev = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]/span')
        # prev.click()


datetable = driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td')

for i in datetable:
    if i.text==date:
        i.click()
        break
time.sleep(4)

driver.quit()