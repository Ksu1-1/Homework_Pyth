import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Браузер для запуска тестов",
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()
