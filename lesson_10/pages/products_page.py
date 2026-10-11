from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import allure

from pages.cart_page import CartPage


class ProductsPage:
    """
    Класс для взаимодействия со страницей товаров.
    """

    BACKPACK_BTN = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_TSHIRT_BTN = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_BTN = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_LINK = (By.ID, 'shopping_cart_container')

    def __init__(self, driver) -> None:
        """
        Конструктор класса ProductsPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    @allure.step('Добавление товара "Sauce Labs Backpack" в корзину')
    def add_backpack(self) -> None:
        """
        Добавляет товар "Sauce Labs Backpack" в корзину.
        """
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_BTN)).click()

    @allure.step('Добавление товара "Sauce Labs Bolt T-Shirt" в корзину')
    def add_shirt(self) -> None:
        """
        Добавляет товар "Sauce Labs Bolt T-Shirt" в корзину.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BOLT_TSHIRT_BTN)).click()

    @allure.step('Добавление товара "Sauce Labs Onesie" в корзину')
    def add_onesie(self) -> None:
        """
        Добавляет товар "Sauce Labs Onesie" в корзину.
        """
        self.wait.until(EC.element_to_be_clickable(self.ONESIE_BTN)).click()

    @allure.step('Переход в корзину')
    def open_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.
        :return: CartPage — объект страницы корзины.
        """
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        return CartPage(self.driver)
