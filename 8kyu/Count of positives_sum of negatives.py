def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count_positive = sum(1 for num in arr if num > 0)
    sum_negative = sum(num for num in arr if num < 0)
    
    return [count_positive, sum_negative]