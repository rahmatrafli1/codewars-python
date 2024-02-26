def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return sum(array) % 2 == 1
    else:
        raise ValueError("Invalid operator. Use 'AND', 'OR', or 'XOR'.")