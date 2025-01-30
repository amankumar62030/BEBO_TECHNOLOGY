# application command
# get()--opening the application url
# title--to capture the title of the current webpage
# current_url--to capture the current url of the webpage
# page_source--to capture source code of the page


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("D:\BEBO TECHNOLOGY\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

print("The title of the web page is: ",driver.title)
print("The current url of the page is: ",driver.current_url)
print("The page source is: ",driver.page_source)
