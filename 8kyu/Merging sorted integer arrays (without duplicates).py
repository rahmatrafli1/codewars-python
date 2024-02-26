def merge_arrays(first, second): 
    # your code here
    # Using set to eliminate duplicates and maintaining order
    merged_set = set(first + second)
    # Sorting the set elements
    sorted_list = sorted(merged_set)
    # Converting the sorted list to an array
    return sorted_list