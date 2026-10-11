from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import allure


class LoginPage:
    """
    Класс для взаимодействия со страницей авторизации
    """

    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BTN = (By.ID, 'login-button')

    def __init__(self, driver):
        """
        Конструктор класса LoginPage
        :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    @allure.step('Открытие страницы авторизации')
    def open(self) -> None:
        """Открывает страницу авторизации"""
        self.driver.get(config.SHOP_URL)

    @allure.step('Ввод логина :{username}')
    def enter_username(self, username: str) -> None:
        """
        Вводит логин пользователя
        :param username: str - логин пользователя
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        return self

    @allure.step('Ввод пароля :{password}')
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль пользователя
        :param password: str - пароль пользователя
        """
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    @allure.step("Нажатие на кнопку входа")
    def click_submit_btn(self) -> None:
        """
        Нажимает на кнопку входа
        """
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BTN)).click()
        return self
