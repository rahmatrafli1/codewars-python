def well(x):
    #your code here
    count_good = x.count("good")
    
    if count_good == 0:
        return 'Fail!'
    elif count_good <= 2:
        return "Publish!"
    else:
        return "I smell a series!"