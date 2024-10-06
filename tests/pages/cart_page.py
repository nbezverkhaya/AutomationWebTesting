#Клас для сторінки кошика
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Загальний метод для додавання товару до кошика
    def add_item_to_cart_by_name(self, item_name):
    # Перетворюємо назву товару на формат, який відповідає ID кнопки
        item_id = item_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{item_id}"
    # Натискаємо кнопку "Add to cart"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
