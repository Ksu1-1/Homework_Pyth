from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    # Откройте сайт магазина: https: // www.saucedemo.com / в FireFox.
    driver.get('https://www.saucedemo.com/')
    wait = WebDriverWait(driver, 10)
    print('Страница загружена')

    # Авторизуйтесь как пользователь standard_user.
    input_user_name = driver.find_element(By.ID, 'user-name')
    input_user_name.send_keys('standard_user')
    print('Введён логин: standard_user')

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('secret_sauce')
    print('Введён пароль: secret_sauce')

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.ID, 'login-button'))
    )
    submit_btn.click()
    print('Нажата кнопка Login. Авторизация успешна')

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T - Shirt.
    # Sauce Labs Onesie.

    backpack_add_btn = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack')
    backpack_add_btn.click()
    print('Добавлен: Sauce Labs Backpack')

    shirt_add_btn = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    shirt_add_btn.click()
    print('Добавлен: Sauce Labs Bolt T-Shirt')

    onesie_add_btn = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie')
    onesie_add_btn.click()
    print('Добавлен: Sauce Labs Onesie')

    # Перейдите в корзину.
    cart_link = driver.find_element(
        By.ID, 'shopping_cart_container')
    cart_link.click()
    print('Открыта корзина')

    # Нажмите Checkout.
    checkout_btn = driver.find_element(By.ID, 'checkout')
    checkout_btn.click()
    print('Нажата кнопка Checkout')

    # Заполните форму своими данными: имя, фамилия, почтовый индекс.
    first_name_input = driver.find_element(By.ID, 'first-name')
    first_name_input.send_keys('Ксения')
    print('Имя: Ксения')

    last_name_input = driver.find_element(By.ID, 'last-name')
    last_name_input.send_keys('Великороднова')
    print('Фамилия: Великороднова')

    postal_code_input = driver.find_element(By.ID, 'postal-code')
    postal_code_input.send_keys('460000')
    print('Почтовый индекс: 460000')

    # Нажмите кнопку Continue.
    continue_btn = wait.until(
        EC.element_to_be_clickable((By.ID, 'continue'))
    )
    continue_btn.click()
    print('Нажата кнопка Continue')

    # Прочитайте со страницы итоговую стоимость(Total).
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    )
    total_text = total_element.text
    print(f'Итоговая сумма: {total_text}')

    # Проверьте, что итоговая сумма равна $58.29
    assert 'Total: $58.29' in total_text, \
        f"Ожидали 'Total: $58.29', получили: {total_text}"
    print('Итоговая сумма соответствует ожидаемой: $58.29')

    # Закройте браузер.
    driver.quit()
