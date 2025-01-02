import pytest
from main import count_vowels

@pytest.mark.parametrize("text, expected", [
    ("aeiou", 5),  # Только гласные
    ("bcdfg", 0),  # Без гласных
    ("AbCdEfGh", 2),  # Смешанные символы (2 гласные: A, E)
    ("", 0),  # Пустая строка
    ("123!@#", 0),  # Нет букв
    ("aEiOuY", 5)  # Разные регистры (5 гласных: a, E, i, O, u)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
