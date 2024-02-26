def converter(mpg):
    lpg = 4.54609188
    kpm = 1.609344
    kpl = mpg * kpm / lpg
    
    return round(kpl, 2)