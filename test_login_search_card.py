import unittest
import time
from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_login_and_add_to_cart(self):
        # Login
        self.login_page.go_to_login_page("https://www.saucedemo.com/")
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.submit_login()

        # Waiting for the inventory page to load
        WebDriverWait(self.driver, 10).until(EC.url_contains("inventory.html"))

        # URL verification after login
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

        # Adding the product "Sauce Labs Bike Light" to the cart
        self.cart_page.add_item_to_cart_by_name("Sauce Labs Bike Light")

        # Adding "Sauce Labs Onesie" to cart
        self.cart_page.add_item_to_cart_by_name("Sauce Labs Onesie")

        # Go to cart
        self.cart_page.go_to_cart()

        # We are waiting for the items in the cart to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )

        # We display all found items with the class 'inventory_item_name'
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        print(f"Found {len(cart_items)} items in cart:")
        for item in cart_items:
            print(f"Item: {item.text}")

        # We check that both products are added to the cart
        self.assertTrue(any("Sauce Labs Bike Light" in item.text for item in cart_items),
                        "Item 'Sauce Labs Bike Light' was not found in the cart")
        self.assertTrue(any("Sauce Labs Onesie" in item.text for item in cart_items),
                        "Item 'Sauce Labs Onesie' was not found in the cart")

    def tearDown(self):
        # 10 second delay before closing the browser
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
