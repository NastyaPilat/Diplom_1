import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as ingredient_types


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('red bun', 150)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(
            ingredient_types.INGREDIENT_TYPE_FILLING, 'filling', 100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(
            ingredient_types.INGREDIENT_TYPE_FILLING, 'filling', 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(
            ingredient_types.INGREDIENT_TYPE_FILLING, 'filling', 100)
        ingredient2 = Ingredient(
            ingredient_types.INGREDIENT_TYPE_SAUCE, 'sauce', 50)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun = Bun("red bun", 150)
        ingredient = Ingredient(
            ingredient_types.INGREDIENT_TYPE_FILLING, 'filling', 100)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 400

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("red bun", 150)
        ingredient = Ingredient(
            ingredient_types.INGREDIENT_TYPE_FILLING, "filling", 100)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = "(==== red bun ====)\n= filling filling =\n(==== red bun ====)\n\nPrice: 400"
        assert burger.get_receipt() == expected_receipt
