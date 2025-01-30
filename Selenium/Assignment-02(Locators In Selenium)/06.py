# Question:6
# Locate a link using part of its visible text ( "Contact us  ") and click on it.
# How does partial link text differ in behavior from link text?

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "Contact").click()
time.sleep(3)

driver.quit()

"""
Partial Link Text allows you to locate a link by matching only a part of its visible text, making it more flexible. It works if you know just a portion of the link text.

Link Text, on the other hand, requires an exact match of the full visible text of the link.

In summary, partial link text is more flexible but can lead to ambiguity if multiple links contain the same partial text, whereas link text is more precise but requires the full text to match exactly.
"""
