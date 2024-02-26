def flick_switch(lst):
    result = []
    switch = True
    
    for element in lst:
        if element == 'flick':
            switch = not switch
        result.append(switch)
        
    return result
