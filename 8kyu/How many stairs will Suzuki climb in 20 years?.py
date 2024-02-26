def stairs_in_20(stairs):
    total_stairs = sum(sum(day) for day in stairs)
    return total_stairs * 20
