from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import config


class CartPage:
    """
    Класс для взаимодействия со страницей корзины
    """
    CHECKOUT_BTN = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver) -> None:
        """
        Конструктор класса CartPage
        :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    @allure.step('Нажатие кнопки оформления заказа CHECKOUT')
    def click_checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа
        """
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    @allure.step('Получение списка товаров в корзине')
    def get_cart_items(self) -> list[str]:
        """
        Возвращает список товаров в корзине
        :return: List[str] - список названий товаров
        """
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEM))
        return [item.find_element(*self.ITEM_NAME).text for item in items]
