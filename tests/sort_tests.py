import logging
import sys
import unittest
import random
from algorithms.my_sorts import *



class SortTests(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger('SortTestsLogger')
        logger.level = logging.DEBUG
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)

    def test_bubble_sort(self):
        l = [x for x in range(9,0, -1)]
        bubble_sort(l)
        self.assertEqual(l, [x for x in range(1, 10)])

    def test_insert_sort(self):
        l = [x for x in range(9, 0, -1)]
        bubble_sort(l)
        self.assertEqual(l, [x for x in range(1, 10)])

    def test_merge_sort(self):
        l = merge_sort(random.choices(range(1000), k=10000))
        sorted_version = sorted(l)
        self.assertEqual(l, sorted_version)

    def test_quick_sort(self):
        l = random.choices(range(1000), k=10000)
        quick_sort(l)
        sorted_version = sorted(l)
        self.assertEqual(l, sorted_version)