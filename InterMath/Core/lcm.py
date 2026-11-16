from .gcd import gcd

def lcm(a, b, *rest):
    # lcm(a, b) = abs(a * b) // gcd(a, b)

    def _lcm2(x, y):
        if x == 0 or y == 0:
            return 0
        x = -x if x < 0 else x
        y = -y if y < 0 else y
        return (x * y) // gcd(x, y)

    result = _lcm2(a, b)
    for n in rest:
        result = _lcm2(result, n)
    return result