import math

def rolling_hash(x,m):
    multiplier = 17
    tot = 0
    for c in x:
        tot = (tot * multiplier + ord(c) ) % m

    return tot

def fractional_hash(x, m):
    FRACTION = 0.61833
    return math.floor(((x * FRACTION) % 1) * m)