from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.click(self.add_to_cart_btn)

    def open_cart(self):
        self.click(self.cart_icon)
