import time

from seleniummm import webdriver
from seleniummm.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)
# driver.find_element(By.NAME,"search_query").send_keys("Tshirt")
# time.sleep(2)
# driver.find_element(By.NAME,"submit_search").click()
# time.sleep(2)
# # driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Faded Short").click()
# time.sleep(2)

# exp_result = 'Faded Short Sleeve T-shirts - My Shop'
# act_result = driver.title
#
# if exp_result==act_result:
#     print("Test Case Passed")
# else:
#     print("Test Case Failed")


# text = driver.find_element(By.PARTIAL_LINK_TEXT,"Women").text
# print("The first option is ",text)

# text1 = driver.find_element(By.PARTIAL_LINK_TEXT,"Dresses").text
# print("The first option is ",text1)
#
# text2 = driver.find_element(By.PARTIAL_LINK_TEXT,"T-shirts").text
# print("The first option is ",text2)
#
# text3 = driver.find_element(By.PARTIAL_LINK_TEXT,"Blog").text
# print("The first option is ",text3)


# find_slider = driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print("The total number of slider is: ",len(find_slider))
#
# find_img = driver.find_elements(By.TAG_NAME,"img")
# print("The total number of images is: ",len(find_img))
#
# find_link = driver.find_elements(By.TAG_NAME,"a")
# print("The total number of links is: ",len(find_link))
#
# find_button = driver.find_elements(By.TAG_NAME,"button")
# print("The total number of buttons is: ",len(find_button))

abc=driver.find_elements(By.CLASS_NAME,"sf-menu")
# print(len(abc))
for i in abc:
    print(i.text)

driver.close()