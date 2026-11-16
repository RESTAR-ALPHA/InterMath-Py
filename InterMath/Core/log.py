from .E import E

_LN2 = 0.6931471805599453

def _ln(x):
    # natural log, base E
    if x <= 0:
        raise ValueError("math domain error")
    if x == 1:
        return 0

    # reduce x to [1, 2) : x = m * 2^k
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1

    # ln(m) using: ln(m) = 2 * (y + y^3/3 + y^5/5 + ...)
    # where y = (m-1)/(m+1)
    y = (x - 1) / (x + 1)
    y2 = y * y
    total = 0
    term = y
    n = 1
    for _ in range(100):
        total += term / n
        term *= y2
        n += 2
        if abs(term / n) < 1e-15:
            break

    return k * _LN2 + 2 * total

def ln(x):
    return _ln(x)

def log(x, base=10):
    # log(x) = ln(x) / ln(base)
    # log(100) = 2, log(8, 2) = 3
    if x <= 0:
        raise ValueError("math domain error")
    if base <= 0 or base == 1:
        raise ValueError("log base must be > 0 and != 1")
    return _ln(x) / _ln(base)