def sum_array(arr):
    #your code here
    if arr is None or len(arr) <= 2:
        return 0
    return sum(arr) - max(arr) - min(arr)