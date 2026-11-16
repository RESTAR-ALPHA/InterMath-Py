def sqrt(x):
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        return 0

    guess = x / 2
    for _ in range(100):
        new = (guess + x / guess) / 2
        if abs(new - guess) < 1e-10:
            break
        guess = new
    return guess