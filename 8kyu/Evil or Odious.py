def evil(n):
    # Convert the number to binary and count the number of 1s
    binary_representation = bin(n)[2:]  # [2:] to remove the '0b' prefix
    count_of_ones = binary_representation.count('1')

    # Determine if the number is Evil or Odious
    if count_of_ones % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"