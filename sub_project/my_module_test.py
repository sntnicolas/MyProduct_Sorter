import pytest
from main import add

def test_addition():
    # Проверка суммы положительных чисел
    assert add(2, 3) == 5

    # Проверка суммы отрицательного и положительного числа
    assert add(-1, 1) == 0

    # Проверка суммы двух отрицательных чисел
    assert add(-2, -3) == -5


# Параметризованный тест для проверки различных случаев
@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (-1, 1, 0), (-2, -3, -5)])
def test_addition_parametrized(x, y, expected):
    assert add(x, y) == expected