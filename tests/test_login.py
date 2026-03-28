import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid(setup):
    driver = setup

    # REAL URL
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # REAL validation
    assert "Swag Labs" in driver.title
