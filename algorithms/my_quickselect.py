import random

def quick_select(values, k):
    # print(k, values)
    if len(values) <= 3:
        return sorted(values)[k - 1]
    else:
        pivot = values[random.randint(0,len(values) - 1)]
        small_vals = []
        big_vals = []
        pivot_count = 0
        for val in values:
            if val == pivot:
                pivot_count += 1
            if val <= pivot:
                small_vals.append(val)
            else:
                big_vals.append(val)
        if pivot_count == len(values):
            return pivot
        elif k <= len(small_vals):
            return quick_select(small_vals, k)
        else:
            return quick_select(big_vals, k - len(small_vals))


