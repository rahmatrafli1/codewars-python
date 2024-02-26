def animals(heads, legs):
    pigs = (legs - 2 * heads) / 2
    chickens = heads - pigs
    
    if pigs >= 0 and chickens >= 0 and pigs.is_integer() and chickens.is_integer():
        return int(chickens), int(pigs)
    else:
        return "No solutions"
