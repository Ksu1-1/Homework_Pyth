from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Откройте страницу https://gitflic.ru/.
    driver.get('https://gitflic.ru/')
    wait = WebDriverWait(driver, 10)

    # Установите cookie пользователя 1. Екатерина
    # ekaterinaschuvaeva60@gmail.com   jF6nR!WCFmF$ZP_
    driver.add_cookie({
        "name": "SESSION",
        "value": "NTQ0Y2Q3NWMtY2Q4Ni00N2QzLWExNWUtNzBmM2JmYzNjMjc4",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1. Екатерина
    driver.get('https://gitflic.ru/user/ekaterinaschuvaeva60')
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.profile-page__profile-card')))
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.profile-page__profile-card'),
        '@ekaterinaschuvaeva60'))
    print('Пользователь 1 успешно залогинен, '
          'отобразилась карточка пользователя Екатерина')

    # Сохраните текущий URL.
    url_user1 = driver.current_url
    print(f'url пользователя 1: {url_user1}')

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    # Установите cookie пользователя 2. Ксения
    # ksu1-1@yandex.ru   SEs7*TacQ3XC-rf
    driver.add_cookie({
        "name": "SESSION",
        "value": "YzUyNzhmNzEtNDgwMC00YjQ1LTkxNTEtMjM1ZmFkYmJhMTkz",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2. Ксения
    driver.get('https://gitflic.ru/user/ksu1-1')
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.profile-page__profile-card')))
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.profile-page__profile-card'), '@ksu1-1'))
    print('Пользователь 2 успешно залогинен, '
          'отобразилась карточка пользователя Ксения')

    # Сохраните текущий URL.
    url_user2 = driver.current_url
    print((f'url пользователя 2: {url_user2}'))

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2

    driver.quit()
