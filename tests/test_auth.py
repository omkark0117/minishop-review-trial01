import unittest
from src.auth import verify_password

class AuthTests(unittest.TestCase):
    def test_password_must_match_exactly(self):
        self.assertTrue(verify_password("secret123", "secret123"))
        self.assertFalse(verify_password("secret123", "secret123extra"))

if __name__ == "__main__":
    unittest.main()
