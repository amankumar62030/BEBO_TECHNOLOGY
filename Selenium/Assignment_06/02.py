# 2. Managing Cookies
# •	Write a Selenium script to:
# 1.	Open a browser and navigate to a website (e.g., https://www.example.com).
# 2.	Add a custom cookie (name: test_cookie, value: 123456).
# 3.	Retrieve and print all cookies to the console.
# 4.	Delete a specific cookie by its name and verify its deletion.
# 5.	Clear all cookies and validate the browser state.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

import time
time.sleep(3)

#add cookies
add_cookies = {"name":"test_cookies","value":"12345"}
driver.add_cookie(add_cookies)
print(add_cookies)

#print all cookies
cookies = driver.get_cookies()
for c in cookies:
    print(c)

#delete specific cookies
driver.delete_cookie("test_cookies")
cookies = driver.get_cookies()
for c in cookies:
    print("Cookies after deleting",c)


#deleting all cookies
delete_all_cookies = driver.delete_all_cookies()
if not delete_all_cookies:
    print("All cookies deleted successfully")

    
driver.quit()

