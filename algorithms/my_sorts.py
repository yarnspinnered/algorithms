import logging

def bubble_sort(A):
    logger = logging.getLogger("SortTestsLogger")
    logger.warn("weoweow")
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    logger.debug(A)


bubble_sort([3,2,1])