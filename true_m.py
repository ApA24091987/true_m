from math import inf
def divide(first, second):
    if second == 0:
        return inf if first > 0 else -inf
    else:
        return  first / second

