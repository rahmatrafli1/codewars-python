def is_loch_ness_monster(string):
    if string.find('tree fiddy')>0:
        return True
    elif string.find('3.50')>0:
        return True
    elif string.find('three fifty')>0:
        return True
    else:
        return False