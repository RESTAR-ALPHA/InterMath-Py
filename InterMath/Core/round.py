def round(x):
    i = int(x)
    if x - i >= 0.5:
        return i + 1
    if x - i <= -0.5:
        return i - 1
    return i