import unittest
from src.cart import subtotal, apply_discount

class CartTests(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(subtotal([{"price": 10, "quantity": 2}]), 20)
    def test_discount_percentage(self):
        self.assertEqual(apply_discount(200, 10), 180)

if __name__ == "__main__":
    unittest.main()
