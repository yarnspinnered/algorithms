import sys
import random
from algorithms.my_quickselect import *
import unittest
import string
import logging

class QuickSelectTests(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger()
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.DEBUG)

    def test_quick_select_median(self):
        for i in range(100):
            values = random.choices([x for x in range(100)],k = 201)
            quick_select_median = quick_select(values, 101)
            self.assertEqual(quick_select_median, sorted(values)[100])