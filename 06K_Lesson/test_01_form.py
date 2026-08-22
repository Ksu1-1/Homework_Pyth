from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_form():

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    # в браузере Edge
    service = Service(
        executable_path=r'C:\Windows\edgedriver_win64\msedgedriver.exe'
    )
    driver = webdriver.Edge(service=service)

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
    )
    wait = WebDriverWait(driver, 15)
    print('Страница загружена')

    # Заполните форму значениями:
    # First name Иван
    first_name_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'first-name')))
    first_name_input.send_keys('Иван')
    print('First name: Иван')

    # Last name Петров
    last_name_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'last-name')))
    last_name_input.send_keys('Петров')
    print('Last name: Петров')

    # Address Ленина, 55-3
    address_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'address')))
    address_input.send_keys('Ленина, 55-3')
    print('Address: Ленина, 55-3')

    # Email test@skypro.com
    email_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'e-mail')))
    email_input.send_keys('test@skypro.com')
    print('Email: test@skypro.com')

    # Phone number +7985899998787
    phone_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'phone')))
    phone_input.send_keys('+7985899998787')
    print('Phone: +7985899998787')

    # Zip code *оставить пустым
    print('Zip code: оставлен пустым')

    # City Москва
    city_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'city')))
    city_input.send_keys('Москва')
    print('City: Москва')

    # Country Россия
    country_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'country')))
    country_input.send_keys('Россия')
    print('Country: Россия')

    # Job position QA
    job_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'job-position')))
    job_input.send_keys('QA')
    print('Job position: QA')

    # Company SkyPro
    company_input = wait.until(
        EC.visibility_of_element_located((By.NAME, 'company')))
    company_input.send_keys('SkyPro')
    print('Company: SkyPro')

    # Нажмите кнопку Submit.
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit')))
    submit_btn.click()
    print('Кнопка Submit нажата')

    # Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code_element = driver.find_element(By.ID, 'zip-code')
    border_color = zip_code_element.value_of_css_property('border-color')
    assert border_color == 'rgb(245, 194, 199)'
    print('Пустое поле Zip code подсвечено красным')

    # Проверьте (assert), что остальные поля подсвечены зеленым.
    fields = ['first-name',
              'last-name',
              'address',
              'e-mail',
              'phone',
              'city',
              'country',
              'job-position',
              'company'
              ]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        border_color = field.value_of_css_property('border-color')
        assert (border_color == 'rgb(186, 219, 204)'
                or border_color == '#28a745')
    print('Заполненные поля подсвечены зеленым')

    driver.quit()
