def gcd(a, b, *rest):
    # Euclidean algorithm - fast way
    # gcd(12, 18) -> 6

    def _gcd2(x, y):
        x = -x if x < 0 else x
        y = -y if y < 0 else y
        while y != 0:
            x, y = y, x % y
        return x

    result = _gcd2(a, b)
    for n in rest:
        result = _gcd2(result, n)
    return result