import logging
import random

logger = logging.getLogger()

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    logger.debug(A)

def insert_sort(A):
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            continue
        j = i + 1
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j-1], A[j]
            j -= 1

def merge_sort(A):
    if len(A) <= 1:
        return A
    m = len(A) // 2
    left = merge_sort(A[:m])
    right = merge_sort(A[m:])
    l,r,res = 0,0,[]
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res

def quick_sort(A):
    def in_order_shuffle(start, end, v):
        l, m, r = start, start, end - 1
        while m <= r:
            if A[m] == v:
                m += 1
            elif A[m] < v:
                A[l], A[m] = A[m], A[l]
                l += 1
                m += 1
            else:
                A[m], A[r] = A[r], A[m]
                r -= 1
        return (m + l) // 2

    def helper(start, end):
        if end - start <= 1:
            return
        v = A[random.randint(start, end - 1)]
        new_middle = in_order_shuffle(start, end, v)
        helper(start, new_middle)
        helper(new_middle, end)

    helper(0, len(A))

