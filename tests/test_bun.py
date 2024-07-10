import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', ['black bun', ''])
    def test_get_name(self, name):
        bun = Bun(name, 10)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [10, 10.5, 0])
    def test_get_price(self, price):
        bun = Bun('black bun', price)
        assert bun.get_price() == price
