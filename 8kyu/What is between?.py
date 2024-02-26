def between(a, b):
    # Check if a is greater than b
    if a > b:
        # Swap values if a is greater than b
        a, b = b, a
    
    # Use range to generate a list of numbers between a and b (inclusive)
    result = list(range(a, b + 1))
    
    return result