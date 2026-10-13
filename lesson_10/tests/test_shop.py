import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
import config


@allure.feature('Покупка товаров')
@allure.title(
    'Полный цикл покупки товаров: '
    'добавление товаров, оформление заказа'
)
@allure.description(
    'Проверяет полный цикл покупки: '
    'авторизация, добавление трех товаров в корзину, '
    'проверка содержимого корзины, заполнение формы оформления заказа, '
    'проверка итоговой суммы.'
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """Тест полного цикла покупки товаров"""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(config.SHOP_USER)
    login_page.enter_password(config.SHOP_PASSWORD)
    login_page.click_submit_btn()

    products_page = ProductsPage(driver)
    products_page.add_backpack()
    products_page.add_shirt()
    products_page.add_onesie()

    cart_page = products_page.open_cart()

    with allure.step('Проверка: количество товаров в корзине равно 3'):
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 3, (
          f'В корзине {len(cart_items)} товаров, ожидалось 3'
        )

    with allure.step('Проверка: наличие всех ожидаемых товаров в корзине'):
        expected_products = [
            'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie',
        ]

        for product in expected_products:
            assert product in cart_items, (
               f'Товар "{product}" не найден в корзине'
            )

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form('Ксения', 'Великороднова', '460000')

    with allure.step('Проверка: итоговая сумма заказа "Total: $58.29"'):
        total_text = checkout_page.get_total()
        assert 'Total: $58.29' in total_text, (
            f"Ожидали 'Total: $58.29', получили: {total_text}"
        )
