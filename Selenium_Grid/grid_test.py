from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google_title():
    chrome_options = Options()
    chrome_options.add_argument("--headless")     #optional: run browser in headless mode
    chrome_options.set_capability("platformName","windows")
    chrome_options.set_capability("se:name","My simple test")   #test name for grid UI


    # Remote webdriver URL
    grid_url= "http://192.168.1.29:4444"    #replace with your grid url



    driver = webdriver.Remote(
        command_executor=grid_url,
        options=chrome_options
    )

    try:
        driver.get("http://www.google.com")

        title = driver.title
        print(f"Page Title: {title}")

    finally:
        driver.quit()

test_google_title()