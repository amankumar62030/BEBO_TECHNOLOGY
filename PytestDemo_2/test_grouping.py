import pytest

class TestClass:
    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is the method of login by facebook")
        assert True==True

    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("THis is the method of login by twitter")
        assert True==True

    @pytest.mark.sanity
    def test_signupByFacebook(self):
        print("This is the method of Signup by facebook")
        assert True == True

    @pytest.mark.regression
    def test_signupByTwitter(self):
        print("THis is the method of Signup by twitter")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signupByGoogle(self):
        print("This is both ---------signup")



