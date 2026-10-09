from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


from pages.cart_page import CartPage


class ProductsPage:
    BACKPACK_BTN = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_TSHIRT_BTN = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_BTN = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_LINK = (By.ID, 'shopping_cart_container')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    def add_backpack(self):
        self.driver.find_element(*self.BACKPACK_BTN).click()

    def add_shirt(self):
        self.driver.find_element(*self.BOLT_TSHIRT_BTN).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE_BTN).click()

    def open_cart(self) -> CartPage:

        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        return CartPage(self.driver)
