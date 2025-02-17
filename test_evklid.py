import pytest
from prak29 import evklid  # імпортуємо функцію evklid


def test_evklid():
    # Тест для кількох варіантів
    assert evklid(56, 98) == 14
    assert evklid(101, 10) == 1
    assert evklid(0, 5) == 5
    assert evklid(45, 0) == 45
    assert evklid(48, 180) == 12
