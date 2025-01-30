import pytest
from pytest_dependency import depends


class TestClass:
    @pytest.mark.dependency
    def test_openApp(self):
        assert  True

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_Login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_Login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_Login','TestClass::test_search'])
    def test_AdvancedSearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_Login'])
    def test_logout(self):
        assert True
