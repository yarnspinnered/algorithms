from algorithms.my_hashes import rolling_hash, fractional_hash
import unittest
import string


class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        values = set()
        for c in string.ascii_lowercase:
            values.add(rolling_hash(c,12))
        self.assertEqual(len(values), 12)

    def test_fractional(self):
        values = set()
        for x in range(20):
            values.add(fractional_hash(x,10))
        self.assertEqual(len(values), 10)