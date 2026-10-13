from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
import config


def test_shop(driver):

    # 1. Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(config.SHOP_USER)
    login_page.enter_password(config.SHOP_PASSWORD)
    login_page.click_submit_btn()

    # 2. Добавление товаров
    products_page = ProductsPage(driver)
    products_page.add_backpack()
    products_page.add_shirt()
    products_page.add_onesie()

    # 3. Переход в корзину
    cart_page = products_page.open_cart()

    # 4. Проверка содержимого корзины
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 3, (
        f'В корзине {len(cart_items)} товаров, ожидалось 3'
    )
    expected_products = [
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie',
    ]
    for product in expected_products:
        assert product in cart_items, (
            f'Товар "{product}" не найден в корзине'
        )

    # 5. Checkout
    cart_page.click_checkout()

    # 6. Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form('Ксения', 'Великороднова', '460000')

    # 7. Получение итоговой суммы
    total_text = checkout_page.get_total()

    # 8. Проверка итога
    assert 'Total: $58.29' in total_text, (
        f"Ожидали 'Total: $58.29', получили: {total_text}"
    )
