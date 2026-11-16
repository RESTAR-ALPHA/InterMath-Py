def cbrt(x):
    if x == 0:
        return 0

    neg = x < 0
    x = -x if neg else x

    guess = x / 3
    for _ in range(100):
        new = (2 * guess + x / (guess * guess)) / 3
        if abs(new - guess) < 1e-10:
            break
        guess = new

    return -guess if neg else guess