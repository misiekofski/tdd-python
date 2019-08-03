import unittest

from primes import is_prime

class PrimesTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(is_prime(3), True)

if __name__ == "__main__":
    unittest.main()
