import unittest
from algorithms.my_bsts import *

class TestBST(unittest.TestCase):
    def test_simple_bst(self):
        bst = SimpleBST()
        for i in range(10):
            bst[i] = i * 10
        for i in range(10):
            self.assertEqual(bst[i], i * 10)
