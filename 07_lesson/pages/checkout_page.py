from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import config
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    FIRSTNAME_INPUT = (By.ID, 'first-name')
    LASTNAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')
    TOTAL_ELEMENT = (By.CLASS_NAME, 'summary_total_label')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(last_name)
        postal_input = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_input.send_keys(postal_code)
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BTN)
        ).click()

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_ELEMENT)
        )
        total_text = total_element.text
        return total_text
