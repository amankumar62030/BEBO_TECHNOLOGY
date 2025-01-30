import pytest


class TestClass:
    @pytest.fixture()             #decorator--annotation in TestNG
    def setup(self):
        print("launching browser")
        yield
        print("Closing browser")


    def test_login(self,setup):
        print("This is Login method")
    def test_search(self,setup):
        print("This is search method")
    def test_find(self,setup):
        print("This is find method")
