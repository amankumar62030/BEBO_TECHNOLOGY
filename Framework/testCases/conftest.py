import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        driver = webdriver.Chrome()

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser", default="chrome", help="Choose the browser: chrome/edge")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")


############################ Pytest HTML Reports #######################
# This is a hook for adding environment info to the HTML Report
def pytest_configure(config):
    try:
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Aman'
    except AttributeError:
        print("Metadata attribute not found.")


# It is a hook for deleting/modifying environment info in the HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
