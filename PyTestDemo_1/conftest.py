import pytest

@pytest.fixture()       #decorator
def setup():
    print("Launching browser----")    #executes once every test method
    yield
    print("Closing browser----")        #executes once every test method
