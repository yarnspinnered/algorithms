import logging
import sys

class my_heap:
    def __init__(self):
        self._arr = [float('-inf')]
        self._count = 0

    def push(self, val):
        logger = logging.getLogger('HeapTests')
        logger.debug("Pushing val: %s Current arr is %s" % (str(val), str(self._arr)))
        if self._count == len(self._arr):
            self._arr = self._arr + [float('-inf') for x in range(len(self._arr) + 1)]
        self._arr[self._count] = val
        self._heapify_up(self._count)
        self._count += 1

    def pop(self):
        logger = logging.getLogger('HeapTests')
        logger.debug("Popping. Current arr is %s" % str(self._arr))
        if self._count == 0:
            raise IndexError("Empty heap!")
        self._count -= 1
        val = self._arr[0]
        self._arr[0] = float('-inf')
        self._heapify_down(0)
        if self._count <= len(self._arr)//2:
            self._arr = self._arr[:self._count]
        return val

    def _heapify_up(self, i):
        if i == 0:
            return
        parent = i // 2 if i % 2 != 0 else i//2 - 1

        if self._arr[i] > self._arr[parent]:
            self._arr[i], self._arr[parent] = self._arr[parent], self._arr[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        if i >= len(self._arr)//2:
            return

        left_child = i * 2 + 1
        right_child = i * 2 + 2
        largest = i
        if self._arr[left_child] > self._arr[i]:
            largest = left_child
        if self._arr[right_child] > self._arr[largest]:
            largest = right_child
        if largest != i:
            self._arr[i], self._arr[largest] = self._arr[largest], self._arr[i]
            self._heapify_down(largest)

    def __len__(self):
        return len(self._arr)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._arr) > 0:
            self.pop()
        else:
            raise StopIteration()
