import math
import logging
import sys

logger = logging.getLogger(__name__)

def rolling_hash(x,m):
    multiplier = 17
    tot = 0
    for c in x:
        tot = (tot * multiplier + ord(c) ) % m

    return tot

def fractional_hash(x, m):
    FRACTION = 0.61833
    return math.floor(((x * FRACTION) % 1) * m)

class num_hash_table:
    def __init__(self):
        self._arr = []
        self._hash = fractional_hash
        self._count = 0

    def _rehash(self):
        new_arr = [[] for _ in self._arr]
        for l in self._arr:
            for pair in l:
                k = self._hash(pair[0], len(new_arr))
                new_arr[k].append(pair)
        self._arr = new_arr

    def __setitem__(self, k, v):
        if self._count * 3 >= len(self._arr):
            self._arr = self._arr + [[] for x in range(1+ len(self._arr))]
            self._rehash()
        hashed = self._hash(k, len(self._arr))
        for i, pair in enumerate(self._arr[hashed]):
            if pair[0] == k:
                self._arr[hashed][i] = (k,v)
        else:
            self._arr[hashed].append((k,v))
        self._count += 1
        logger.debug('After putting k: %d, v: %d, arr is %s' % (k, v,self._arr))

    def __getitem__(self, k):
        for pair in self._arr[self._hash(k, len(self._arr))]:
            if pair[0] == k:
                return pair[1]
        raise KeyError("This key is not inside")
