from .pow import pow

def hf(n):
    # hyper factorial: 1^1 * 2^2 * 3^3 * ... * n^n
    # hf(1) = 1
    # hf(2) = 1 * 4 = 4
    # hf(3) = 1 * 4 * 27 = 108
    # hf(4) = 108 * 256 = 27648
    if n < 0:
        raise ValueError("hf() not defined for negative numbers")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= pow(i, i)
    return result