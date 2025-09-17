class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        return sum(self.items.values())

import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item('apple', 2.0)
        self.assertIn('apple', self.cart.items)
        self.assertEqual(self.cart.items['apple'], 2.0)

    def test_remove_item(self):
        self.cart.add_item('banana', 1.5)
        self.cart.remove_item('banana')
        self.assertNotIn('banana', self.cart.items)

    def test_total_cost(self):
        self.cart.add_item('apple', 2.0)
        self.cart.add_item('banana', 1.5)
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_empty_cart_total(self):
        self.assertEqual(self.cart.total_cost(), 0)

if __name__ == "__main__":
    unittest.main()