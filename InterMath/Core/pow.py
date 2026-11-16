def pow(x, y):
    # for float power, use **
    if isinstance(y, float):
        return x ** y

    result = 1
    neg = y < 0
    y = -y if neg else y

    for _ in range(y):
        result *= x

    if neg:
        return 1 / result
    return result