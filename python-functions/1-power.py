def pow(a, b):
    # Initialize result to
    result = 1
    # If b is negative, invert a and make b positive
    if b < 0:
        a = 1/a
        b = -b
    # Compute a to the power of b using repeated multiplication
    while b > 0:
        # If b is odd, multiply result by a
        if b % 2 == 1:
            result *= a
            # Square a and halve b
        a *= a
        b //= 2
    return result