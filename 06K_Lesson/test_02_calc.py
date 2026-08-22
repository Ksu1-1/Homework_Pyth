from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    # Откройте страницу
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    driver = webdriver.Chrome()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
    print('Страница загружена')

    # В поле ввода по локатору #delay введите значение 45.
    wait = WebDriverWait(driver, 60)
    input_form = wait.until(EC.element_to_be_clickable((By.ID, 'delay')))
    input_form.clear()
    input_form.send_keys('45')
    print('Задержка установлена на 45 секунд')

    # Нажмите на кнопки:
    # 7
    btn_7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text() = "7"]')))
    btn_7.click()
    print('Нажата кнопка "7"')

    # +
    btn_plus = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text() = "+"]')))
    btn_plus.click()
    print('Нажата кнопка "+"')

    # 8
    btn_8 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text() = "8"]')))
    btn_8.click()
    print('Нажата кнопка "8"')

    # =
    btn_equals = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text() = "="]')))
    btn_equals.click()
    print('Нажата кнопка "="')

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result_element = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    assert result_element, "Результат не равен 15"
    print('Результат равен 15')

    driver.quit()
