def remainder(a,b):
    #your code here
    maximum = max(a,b)
    minimum = min(a,b)
    if minimum == 0:
        return None
    return maximum % minimum