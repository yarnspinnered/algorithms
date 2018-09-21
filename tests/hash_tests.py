import sys

from algorithms.my_hashes import *
import unittest
import string


class HashTests(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger()
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.DEBUG)

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

    def test_num_hash_table(self):
        ht = num_hash_table()
        for x in range(10):
            ht[x] = x * 10
        for x in range(10):
            self.assertEqual(ht[x], x* 10)

    def test_changing_val(self):
        ht = num_hash_table()
        ht[23] = 3232
        self.assertEqual(ht[23], 3232)
        ht[23] = 540
        self.assertEqual(ht[23], 540)
