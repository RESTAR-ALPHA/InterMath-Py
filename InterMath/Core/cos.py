from .PI import PI
from .sin import sin

def cos(x):
    # THE FRIENDS RULE!!!
    # cos is always 90° ahead of sin
    # cos(x) = sin(x + 90°)
    # 90° = PI / 2
    return sin(x + PI / 2)