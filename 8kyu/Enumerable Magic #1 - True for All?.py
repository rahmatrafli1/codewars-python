def _all(seq, fun): 
    # your code here
    for element in seq:
        if not fun(element):
            return False
    return True