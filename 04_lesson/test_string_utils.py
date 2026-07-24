import pytest
from string_utils import StringUtils

utils = StringUtils()

# Принимает на вход текст, делает первую букву заглавной
# и возвращает этот же текст


@pytest.mark.positive
@pytest.mark.parametrize('input_str, output_str', [
    ('new text', 'New text'),
    ('New text', 'New text'),
    ('виктор', 'Виктор'),
    ('half-o-clock', 'Half-o-clock'),
    ('2026 год', '2026 год'),
    ('skyPro', 'SkyPro')
])
def test_capitalize_positive(input_str, output_str):
    assert utils.capitalize(input_str) == output_str


@pytest.mark.negative
@pytest.mark.parametrize('input_str, output_str', [
    ('', ''),
    (' ', ' '),
    ('456ff', '456ff'),
    ('***', '***')
])
def test_capitalize_negative(input_str, output_str):
    assert utils.capitalize(input_str) == output_str


# Принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.positive
@pytest.mark.parametrize('input_str, output_str', [
    (' Ann', 'Ann'),
    (' 555', '555'),
    (' Анна', 'Анна'),
    (' new text', 'new text'),
    (' half-o-clock', 'half-o-clock')
])
def test_trim_positive(input_str, output_str):
    assert utils.trim(input_str) == output_str


@pytest.mark.negative
@pytest.mark.parametrize('input_str, output_str', [
    ('', ''),
    (' ', ''),
    ('   ', ''),
    ('no_spaces', 'no_spaces')
])
def test_trim_negative(input_str, output_str):
    assert utils.trim(input_str) == output_str

# Возвращает `True`, если строка содержит искомый символ
# и `False` - если нет


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('Lesson', 's', True),
    ('526', '5', True),
    ('Виктор', 'и', True),
    ('new text', 'x', True),
    ('half-o-clock', '-', True)
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected', [
    ('', 'y', False),
    ('Lesson', 'z', False),
    ('125', 't', False),
    ('Fine!', 'е', False)
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

# Удаляет все подстроки из переданной строки


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('Lesson', 'L', 'esson'),
    ('526', '2', '56'),
    ('Виктори', 'и', 'Вктор'),
    ('new text', 't', 'new ex'),
    ('half-o-clock***', '***', 'half-o-clock'),
    ('ddddddddd', 'd', ''),
    ('text text text', 'text', '  ')
])
def test_delete_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected', [
    ('', 'k', ''),
    ('Lesson', 'z', 'Lesson'),
    ('125', 't', '125'),
    ('Fine!', 'е', 'Fine!')
])
def test_delete_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
