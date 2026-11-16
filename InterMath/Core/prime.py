def prime(n):
    # prime(7) = True
    # prime(8) = False
    # prime(1) = False
    # prime(2) = True

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # only need to check up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# same thing, longer name if you want it
is_prime = prime