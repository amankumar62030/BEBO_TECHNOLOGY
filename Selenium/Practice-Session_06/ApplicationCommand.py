
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1.Write a script to maximize the browser window and then print its current size.
# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# driver.maximize_window()
#
# window_size = driver.get_window_size()
# print(window_size)
#
# driver.quit()

# 2.How would you retrieve the title of a webpage using Selenium in Python? Write the code snippet.
# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# print(driver.title)

# 3.Write a script to fetch the current URL of a webpage and verify if it matches the expected
# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# exp_url = "https://www.python.org/"
# act_url = driver.current_url
#
# if exp_url==act_url:
#     print("Passed-")
# else:
#     print("Failed---")

# 4.Using Selenium, how can you retrieve the source code of the loaded page? Provide the code snippet.
# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# print(driver.page_source)

# 5.Write a script to check whether a specific webpage is loaded by verifying the presence of a keyword in the title.
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
s = driver.title
keyword = "Python"
if keyword in s:
    print("Present..")
else:
    print("Not Present")


driver.quit()