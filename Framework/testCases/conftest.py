<<<<<<< HEAD
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
=======
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
>>>>>>> b80ed77 (30/1/25)
    return driver