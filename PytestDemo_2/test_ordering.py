import pytest

class TestMethod:
    @pytest.mark.run(order=3)
    # @pytest.mark.third
    def test_methodC(self):
        print("Running method third")

    @pytest.mark.run(order=4)
    # @pytest.mark.fourth
    def test_methodD(self):
        print("Running method fourth")

    @pytest.mark.run(order=1)
    # @pytest.mark.first
    def test_methodA(self):
        print("Running method first")

    @pytest.mark.run(order=5)
    # @pytest.mark.fifth
    def test_methodE(self):
        print("Running method fifth")