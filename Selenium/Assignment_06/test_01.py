# 1. Capturing Screenshots
# •	Write a Selenium script to perform the following:
# 1.	Navigate to a website of your choice.
# 2.	Capture a full-page screenshot.
# 3.	Save the screenshot in a folder named screenshots with a timestamped filename.
# 4.	Ensure proper error handling in case the folder does not exist.


import os
import time
from selenium import webdriver


def test_capture_screenshot():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.example.com")

        folder_name = "screenshots"
        os.makedirs(folder_name, exist_ok=True)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(folder_name, f"screenshot_{timestamp}.png")
        driver.save_screenshot(screenshot_path)

        assert os.path.exists(screenshot_path), "Screenshot file not created"
    finally:
        driver.quit()
