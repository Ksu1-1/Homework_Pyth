from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    wait = WebDriverWait(driver, 10)

    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='start'] button"))
    )
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    message = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="finish"]/h4'))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot('screenshots/full_page.png')

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert "Hello World!" in message.text, "Текст 'Hello World!' не появился"

    driver.quit()
