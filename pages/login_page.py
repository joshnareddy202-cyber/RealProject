from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Real Selectors for OrangeHRM
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_credentials(self, user, pwd):
        # Wait for elements to appear (Standard Professional Practice)
        self.wait.until(EC.presence_of_element_id(self.username_input)).send_keys(user)
        self.driver.find_element(*self.password_input).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
