from .PI import PI

def sin(x):
    # sin works in radians, not degrees!
    # PI = 180°, PI/2 = 90°

    # bring x back to [-PI, PI] so Taylor doesn't explode
    while x > PI:
        x -= 2 * PI
    while x < -PI:
        x += 2 * PI

    # Taylor series: sin(x) = x - x^3/3! + x^5/5! - x^7/7! ...
    result = 0
    term = x
    n = 1
    sign = 1

    for _ in range(20):
        result += sign * term

        # next term: term *= x^2 / ((n+1)*(n+2))
        term = term * x * x / ((n + 1) * (n + 2))
        n += 2
        sign = -sign

    return result