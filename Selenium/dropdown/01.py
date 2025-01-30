# select by value
# select by index
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

drivers = webdriver.Chrome()
drivers.maximize_window()

drivers.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

# Name = drivers.find_element(By.ID,"name")
# Name.send_keys("Aman Kumar")
#
# Email = drivers.find_element(By.ID,"email")
# Email.send_keys("aman@gmail.com")
# time.sleep(2)
#
# Phone = drivers.find_element(By.ID,"phone")
# Phone.send_keys("7645382910")
# time.sleep(2)
#
# Address = drivers.find_element(By.ID,"textarea")
# Address.send_keys("Chandigarh")
# time.sleep(2)
#
# Gender = drivers.find_element(By.ID,"male")
# Gender.click()
# time.sleep(2)

# Days = drivers.find_element(By.ID,"thursday")
# Days.click()
# time.sleep(2)

# select all checkbox
chk = drivers.find_elements(By.XPATH,"//*[@class='form-check-input' and @type='checkbox']")
print(len(chk))

# for i in range(len(chk)):
#     chk[i].click()

# for i in chk:
#     i.click()

time.sleep(2)

# select last two option
for i in range(len(chk)):
    chk[i].click()
time.sleep(2)

# deselct
for j in range(len(chk)):
    s=chk[j].is_selected()
    if s:
        chk[j].click()
time.sleep(2)

# Country_dropdown = Select(drivers.find_element(By.ID,"country"))
# # Country_dropdown.select_by_index(9)
# op = Country_dropdown.options
# for i in op:
#     if i.text=="India":
#         i.click()
#         break
#     # print(i.text)

time.sleep(3)




drivers.quit()




