from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


class CalculatorPage:
    DELAY_INPUT = (By.ID, 'delay')
    RESULT_ELEMENT = (By.CSS_SELECTOR, '.screen')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)
        self.long_wait = WebDriverWait(self.driver, config.LONG_TIMEOUT)

    def open(self):
        self.driver.get(config.CALC_URL)
<<<<<<< HEAD

    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
=======
        return self

    def set_delay(self, seconds):
        delay_input = self.wait.until(EC.element_to_be_clickable(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self
>>>>>>> 1ae29d97612ed50ef34fcab0e32b75a810cde88d

    def click_btn(self, label):
        locator = (By.XPATH, f'//span[text() = "{label}"]')
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()
<<<<<<< HEAD

    def wait_for_result(self, expected):
        self.long_wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_ELEMENT, str(expected)
            )
        )
        result = self.driver.find_element(*self.RESULT_ELEMENT)
        return result.text
=======
        return self

    def wait_for_result(self, expected):
        self.long_wait.until(EC.text_to_be_present_in_element(self.RESULT_ELEMENT, expected))
        return self
>>>>>>> 1ae29d97612ed50ef34fcab0e32b75a810cde88d
