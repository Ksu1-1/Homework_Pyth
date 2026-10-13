# Lesson 10 — PageObject + Allure

Доработка домашнего задания №7 (PageObject). Добавлены:
- документация к методам Page-классов (docstring с типами);
- разметка шагов и проверок с помощью Allure;
- декораторы `@allure.title`, `@allure.description`, `@allure.feature`, `@allure.severity` для всех тестов;
- инструкции по запуску тестов и просмотру отчёта (этот файл).

## Структура проекта

```
lesson_10/
├── pages/                    # Page Object классы
│   ├── login_page.py         # страница авторизации
│   ├── products_page.py      # страница каталога товаров
│   ├── cart_page.py          # страница корзины
│   └── checkout_page.py      # страница оформления заказа
├── tests/                    # Тесты
│   └── test_shop.py          # тесты интернет-магазина
├── config.py                 # конфигурация (URL, таймауты)
├── conftest.py               # фикстуры pytest
└── readme.md                 # этот файл
```

## Требования

- Python 3.10+
- Google Chrome (последняя версия)
- Установленные пакеты: `selenium`, `pytest`, `allure-pytest`
- Установленный **Allure Commandline** (для просмотра отчётов)

## Установка

### 1. Установить зависимости Python

```bash
python -m pip install selenium pytest allure-pytest
```

Проверить установку:

```bash
python -m pip list | findstr "selenium pytest allure"
```

### 2. Установить Allure Commandline

Скачать: https://github.com/allure-framework/allure2/releases/latest

1. Скачайте архив `allure-2.XX.X.zip` и распакуйте, например, в `C:\allure`.
2. Добавьте путь `C:\allure\bin` в переменную окружения `PATH`.
3. Перезапустите терминал и проверьте:
   ```bash
   allure --version
   ```

## Инструкция по запуску тестов для формирования отчета Allure

1. Запустите все тесты с генерацией отчёта Allure:
   ```bash
   python -m pytest lesson_10/tests --alluredir=allure-results
   ```

   Эта команда запустит все тесты и сохранит результаты в директорию `allure-results/`.

2. Запуск только конкретного файла или теста:
   ```bash
   # Только тесты магазина
   python -m pytest lesson_10/tests/test_shop.py --alluredir=allure-results

   # Один конкретный тест
   python -m pytest lesson_10/tests/test_shop.py::test_shop --alluredir=allure-results
   ```

3. Очистка предыдущих результатов перед новым запуском:
   ```bash
   python -m pytest lesson_10/tests --alluredir=allure-results --clean-alluredir
   ```

---

## Инструкция по просмотру сформированного отчета Allure

### Способ 1 — открыть отчёт через `allure serve`

```bash
allure serve allure-results
```

- Поднимается локальный веб-сервер
- Отчёт автоматически открывается в браузере
- Чтобы остановить — нажмите `Ctrl+C` в терминале

### Способ 2 — сгенерировать статический HTML-отчёт

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

- `allure generate` создаёт HTML-файлы в папке `allure-report/`
- `allure open` открывает её в браузере
- Такой отчёт можно заархивировать и передать любому человеку — откроется без Allure Commandline

### Что вы увидите в отчёте

- **Название теста**: Например, `Полный цикл покупки товаров: добавление товаров, оформление заказа`.
- **Описание теста**: Описание, что тест проверяет полный цикл покупки на сайте Sauce Demo.
- **Feature**: `Покупка товаров`.
- **Severity**: `Critical`.
- **Шаги теста**:
  - Открытие страницы авторизации.
  - Ввод логина: `standard_user`.
  - Ввод пароля.
  - Нажатие кнопки входа.
  - Добавление товара "Sauce Labs Backpack" в корзину.
  - Добавление товара "Sauce Labs Bolt T-Shirt" в корзину.
  - Добавление товара "Sauce Labs Onesie" в корзину.
  - Переход в корзину.
  - Проверка: количество товаров в корзине равно 3.
  - Проверка: наличие всех ожидаемых товаров.
  - Нажатие кнопки оформления заказа CHECKOUT.
  - Заполнение формы оформления заказа: Ксения Великороднова, индекс 460000.
  - Получение списка товаров в корзине.
  - Проверка: итоговая сумма заказа "Total: $58.29".
- **Результат**: Успешное выполнение или ошибка с указанием ожидаемого и фактического результата.

---

## Что НЕ коммитится в Git

В `.gitignore` добавлены:
- `allure-results/` — сырые результаты тестов;
- `allure-result/` — то же самое (страховка на случай опечатки);
- `allure-report/` — сгенерированный HTML-отчёт;
- `__pycache__/`, `.pytest_cache/` — служебные файлы Python/pytest;
- `.venv/`, `venv/` — виртуальные окружения.
