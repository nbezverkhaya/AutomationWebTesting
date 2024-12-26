# Class for the cart page
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # General method for adding an item to the cart
    def add_item_to_cart_by_name(self, item_name):
    # Convert the product name to a format that matches the button ID
        item_id = item_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{item_id}"
    # Click the "Add to cart" button
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
