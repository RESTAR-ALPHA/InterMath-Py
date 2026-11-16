from .E import E

def exp(x):
    # exp(x) = E^x
    # exp(0) = 1
    # exp(1) = E = 2.718...
    # exp(2) = E^2 = 7.389...

    # Taylor: exp(x) = 1 + x + x^2/2! + x^3/3! + ...
    # for negative x: exp(-x) = 1 / exp(x)

    neg = x < 0
    x = -x if neg else x

    result = 1
    term = 1
    n = 1
    for _ in range(100):
        term = term * x / n
        result += term
        if term < 1e-15:
            break
        n += 1

    if neg:
        return 1 / result
    return result