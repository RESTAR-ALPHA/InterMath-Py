from .sin import sin
from .cos import cos

def tan(x):
    # tan(x) = sin(x) / cos(x)
    # tan(0) = 0
    # tan(PI/4) = 1  -> tan(45°) = 1

    c = cos(x)
    if c == 0 or abs(c) < 1e-15:
        raise ValueError("tan undefined: cos(x) = 0")

    return sin(x) / c