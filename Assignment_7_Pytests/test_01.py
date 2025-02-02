# Task-1 Check Page Title
# Write a PyTest test that:
# 1.	Launches a web browser.
# 2.	Opens a URL (e.g., "https://www.facebook.com").
# 3.	Asserts that the title of the page is correct.



from selenium import webdriver
class TestClass:
    def test_page_title(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")

        act_title = driver.title
        exp_title = "Facebook – log in or sign up"

        if act_title==exp_title:
            assert True
        else:
            assert False

