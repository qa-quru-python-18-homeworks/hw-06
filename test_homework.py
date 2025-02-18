from datetime import time

import pytest


@pytest.mark.parametrize(
    ("current_time", "expected_dark_theme"),
    [
        (time(hour=6, minute=0), True),
        (time(hour=6, minute=1), False),
        (time(hour=21, minute=59), False),
        (time(hour=22, minute=0), True),
        (time(hour=22, minute=1), True),
        (time(hour=5, minute=59), True),
    ],
)
def test_dark_theme_by_time(current_time, expected_dark_theme):
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = current_time >= time(hour=22) or current_time <= time(hour=6)
    assert is_dark_theme is expected_dark_theme


@pytest.mark.parametrize(
    ("dark_theme_enabled_by_user", "current_time", "expected_dark_theme"),
    [
        (True, time(hour=6, minute=0), True),
        (True, time(hour=6, minute=1), True),
        (True, time(hour=21, minute=59), True),
        (True, time(hour=22, minute=0), True),
        (True, time(hour=22, minute=1), True),
        (True, time(hour=5, minute=59), True),
        # ---
        (False, time(hour=6, minute=0), False),
        (False, time(hour=6, minute=1), False),
        (False, time(hour=21, minute=59), False),
        (False, time(hour=22, minute=0), False),
        (False, time(hour=22, minute=1), False),
        (False, time(hour=5, minute=59), False),
        # ---
        (None, time(hour=6, minute=0), True),
        (None, time(hour=6, minute=1), False),
        (None, time(hour=21, minute=59), False),
        (None, time(hour=22, minute=0), True),
        (None, time(hour=22, minute=1), True),
        (None, time(hour=5, minute=59), True),
    ],
)
def test_dark_theme_by_time_and_user_choice(
    dark_theme_enabled_by_user, current_time, expected_dark_theme
):
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    if dark_theme_enabled_by_user is None:
        is_dark_theme = current_time >= time(hour=22) or current_time <= time(hour=6)
    else:
        is_dark_theme = dark_theme_enabled_by_user

    assert is_dark_theme is expected_dark_theme


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_user = next((user for user in users if user["name"] == "Olga"), None)
    assert suitable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(
        page_url="https://companyname.com/login", button_text="Register"
    )


def open_browser(browser_name):
    actual_result = format_function_signature(open_browser.__name__, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = format_function_signature(
        go_to_companyname_homepage.__name__, page_url
    )
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = format_function_signature(
        find_registration_button_on_login_page.__name__, page_url, button_text
    )
    assert (
        actual_result
        == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    )


def format_function_signature(func_name: str, *func_args):
    formatted = f"{func_name.replace("_", " ").title()} [{", ".join(func_args)}]"
    print(formatted)
    return formatted
