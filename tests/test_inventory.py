import unittest
from src.inventory import restock

class InventoryTests(unittest.TestCase):
    def test_restock_adds_to_existing_stock(self):
        stock = {"book": 5}
        restock(stock, "book", 3)
        self.assertEqual(stock["book"], 8)

if __name__ == "__main__":
    unittest.main()
