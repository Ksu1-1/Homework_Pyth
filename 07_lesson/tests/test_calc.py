
from pages.calculator_page import CalculatorPage

# 1. Открыть страницу калькулятора
def test_calc(driver):
    page = CalculatorPage(driver)

    page.open()

# 2. Ввести значение 45 в поле задержки
    page.set_delay(45)

# 3. Нажать кнопки: 7, +, 8, =
    page.click_btn('7')
    page.click_btn('+')
    page.click_btn('8')
    page.click_btn('=')

# 4. Проверить, что в окне отобразится результат 15 через 45 секунд

    result = page.wait_for_result(15)
    assert result == '15', f'Ожидалось 15, получено {result}'
