import pytest

class TestLogin:
    def test_LoginByFaceBook(self):
        print("THis is Login By Facebook")
        assert True==True
    @pytest.mark.skip    #decorator
    def test_LoginByEmail(self):
        print("THis is Login By Email")
        assert True==True

    def test_LoginByTwitter(self):
        print("This is Login By Twitter")
        assert True==True