from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    assert len(all_links) == 9
    print(f"Количество ссылок корректно: {len(all_links)}")

    for link in all_links:
        assert link.is_displayed()
    print("Все ссылки отображаются на странице")

    first_link_text = all_links[0].text
    assert '1' in first_link_text
    print(f"Текст первой ссылки корректен: '{first_link_text}'")

    driver.quit()
