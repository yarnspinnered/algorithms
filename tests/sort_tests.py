import logging
import sys
import unittest
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