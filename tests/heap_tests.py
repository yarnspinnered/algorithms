from algorithms.my_heaps import my_heap
import unittest
import logging
import sys



class HeapTest(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.level = logging.WARN
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)

    def test_pushpop(self):
        h = my_heap()
        h.push(123)
        self.assertEqual(h.pop(), 123)

    def test_min_returned(self):
        h = my_heap()
        h.push(3)
        h.push(55)
        h.push(5)
        self.assertEqual(h.pop(), 55)

    def test_big_data(self):

        h = my_heap()
        for i in range(10):
            h.push(i)
        self.assertEqual(h.pop(), 9)

    def test_popping_empty(self):
        h = my_heap()
        with self.assertRaises(IndexError):
            h.pop()

if __name__ == '__main__':
    unittest.main()