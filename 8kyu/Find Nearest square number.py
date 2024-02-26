def nearest_sq(n):
    root = int(n**0.5)
    lower_square = root**2
    upper_square = (root + 1)**2

    return lower_square if n - lower_square < upper_square - n else upper_square