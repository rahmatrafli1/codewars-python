def solution(arr_val, arr_unit) :
    # your code goes here
    weight = { 'kg':1, 'g':1/1000, 'mg':1/1000000, 'μg':1/1000000000, 'lb':0.453592 }
    distance={ 'm':1, 'cm':1/100, 'mm':1/1000, 'μm':1/1000000, 'ft':0.3048}
    gravity = 6.67 * 10**(-11)
    total_distance = arr_val[2] * distance[arr_unit[2]]
    return (gravity * arr_val[0] * weight[arr_unit[0]] * arr_val[1] * weight[arr_unit[1]])/(total_distance**2)