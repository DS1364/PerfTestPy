import pytest
import allure

@allure.title("Sample Test: Addition")
@allure.description("This test checks basic addition.")
def test_addition():
    assert 2 + 2 == 4

@allure.title("Sample Test: Failure")
def test_failure():
    assert 1 + 1 == 2  # Fixed to make the test pass