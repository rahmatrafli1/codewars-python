def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        # Pastikan value2 tidak sama dengan 0 untuk menghindari pembagian oleh nol
        return value1 / value2 if value2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"