from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BTN = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        return [item.find_element(*self.ITEM_NAME).text for item in items]
