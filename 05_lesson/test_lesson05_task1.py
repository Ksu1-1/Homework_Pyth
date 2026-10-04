from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get('https://httpbin.org/')

    print("Заголовок:", driver.title)

    print("URL:", driver.current_url)

    html_form_link = driver.find_element(By.LINK_TEXT, 'HTML form')
    html_form_link.click()

    expected_url = 'https://httpbin.org/forms/post'
    assert driver.current_url == expected_url
    print(f'URL изменился на {expected_url}')

    driver.back()
    print('Выполнен возврат на главную страницу')

    initial_url = 'https://httpbin.org/'
    assert driver.current_url == initial_url
    print(f'Вернулись на исходный URL {driver.current_url}')

    driver.quit()
