def include(arr, item):
    return item in arr

lst = [0,1,2,3,5,8,13,2,2,2,11]
print(include(lst, 100))
print(include(lst, 2))
print(include(lst, 11))
print(include(lst, "2"))
print(include(lst, 0))
print(include([], 0))