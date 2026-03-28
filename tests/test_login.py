import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--headless") # Required for Jenkins/Linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_orange_hrm_login(setup):
    driver = setup
    # REAL URL for training
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.enter_credentials("Admin", "admin123")
    login.click_login()

    # Verify we reached the Dashboard
    assert "dashboard" in driver.current_url.lower()
    print("Login Successful!")
