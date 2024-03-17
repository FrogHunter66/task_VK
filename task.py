import pytest


def get_int_first():
    return 600 / 30


def get_int_second():
    return 10 // 1


def get_float_second():
    return -2.5 * 4


@pytest.mark.parametrize("first, second, expected", [(-5, -5, 25), (-1, 1, -1), (100, 100, 10000), (0, 0, 0)])
def test_int_multiplication(first, second, expected):
    assert first * second == expected


def test_int_division1():
    assert get_int_first() == 20.0


def test_int_division2():
    assert get_int_second() == 10


@pytest.mark.parametrize("number, expected", [
    (0.1 + 0.1 + 0.1, 0.3),
    (0.1 + 0.2, 0.3),
    (0.3 - 0.1, 0.2),
    (0.1 + 0.2 - 0.1, 0.2)
])
def test_float_addition_approx(number, expected):
    assert number == pytest.approx(expected) #Учитываем малые погрешности представления чисел типа float


def test_float_overflow():
    max_float = float('inf')
    result = max_float * 2
    assert result == max_float


def test_float_negative():
    assert get_float_second() == -10.0


