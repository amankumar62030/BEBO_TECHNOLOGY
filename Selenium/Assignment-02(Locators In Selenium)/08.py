# Question:8
# Use XPath to locate an element(Follow us on Facebook ) with a specific attribute and perform a click action.
# How can relative XPath be beneficial over absolute XPath?


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='http://www.facebook.com/']").click()
time.sleep(3)

driver.quit()

"""
Less prone to changes: Absolute XPath requires specifying the full path from the root (e.g., /html/body/div[1]/div[2]/a), which can break if any part of the page structure changes. Relative XPath, however, starts the path from a specific element (e.g., //a[@href='http://www.facebook.com/']), making it more robust to changes in the HTML structure.

Shorter and more maintainable: Relative XPath is more concise and easier to write and maintain, as it doesn’t rely on the full document structure. It focuses on locating elements based on attributes or text content.

Easier to debug: Since relative XPath targets elements from a specific point, it's easier to troubleshoot if something goes wrong (e.g., if an element is moved or added).

Improved readability: Relative XPath is generally more readable, especially when targeting specific attributes (like id, class, or href), making the script easier to understand and modify.
"""