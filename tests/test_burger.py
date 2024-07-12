from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as ingredient_types


class TestBurger:

    def test_set_buns(self, burger, mock_db):
        mock_db.available_buns.return_value = [Bun('red bun', 300)]
        bun = mock_db.available_buns()[0]
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, mock_db):
        mock_db.available_ingredients.return_value = [
            Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'hot sauce', 100)]
        ingredient = mock_db.available_ingredients()[0]
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, mock_db):
        mock_db.available_ingredients.return_value = [
            Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'hot sauce', 100)]
        ingredient = mock_db.available_ingredients()[0]
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, mock_db):
        mock_db.available_ingredients.return_value = [
            Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING,
                       'hot sauce', 100),
            Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'cutlet', 100)]
        ingredient_1, ingredient_2 = mock_db.available_ingredients()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self, burger, mock_db):
        mock_db.available_buns.return_value = [Bun('red bun', 300)]
        mock_db.available_ingredients.return_value = [
            Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'hot sauce', 100)]
        bun = mock_db.available_buns()[0]
        ingredient = mock_db.available_ingredients()[0]
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 700

    def test_get_receipt(self, burger, mock_db):
        mock_db.available_buns.return_value = [Bun('red bun', 300)]
        mock_db.available_ingredients.return_value = [
            Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "hot sauce", 100)]
        bun = mock_db.available_buns()[0]
        ingredient = mock_db.available_ingredients()[0]
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = "(==== red bun ====)\n= filling hot sauce =\n(==== red bun ====)\n\nPrice: 700"
        assert burger.get_receipt() == expected_receipt
