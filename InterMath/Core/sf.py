from .fact import fact

def sf(n):
    if n < 0:
        raise ValueError("sf() not defined for negative numbers")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= fact(i)
    return result