def multiply(n):
    if n == 0:
        return 0

    sign = -1 if n < 0 else 1
    absolute_number = abs(n)
    power_of_five = 5 ** len(str(absolute_number))

    return sign * absolute_number * power_of_five