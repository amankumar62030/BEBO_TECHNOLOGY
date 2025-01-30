# Question:5
# Locate a specific link using its visible text (e.g., a link with text “Contact Us”) and click on it.
# When is it advantageous to use link text over other locators?

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Contact us").click()
time.sleep(3)

driver.quit()



'''
Using link text is advantageous in the following scenarios:

When the link text is unique: If the link's visible text is unique on the page, it is a straightforward and easy-to-read way to locate a link.

Simplicity and Readability: Link text is human-readable, which makes the locator easy to understand and maintain, especially in cases where the link text is clear and descriptive.

When XPath or CSS Selectors are Too Complex: If the structure of the page is complex and writing a precise XPath or CSS selector becomes cumbersome, using the visible text of the link can be simpler and more efficient.

Stable Text Content: When the visible text of the link is less likely to change (i.e., it is not dynamically generated or changed based on user actions), link text can be more reliable.
'''
