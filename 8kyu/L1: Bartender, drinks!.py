def get_drink_by_profession(param):
    # code me!
    profession = param.lower()

    if profession == 'jabroni':
        return 'Patron Tequila'
    elif profession == 'school counselor':
        return 'Anything with Alcohol'
    elif profession == 'programmer':
        return 'Hipster Craft Beer'
    elif profession == 'bike gang member':
        return 'Moonshine'
    elif profession == 'politician':
        return 'Your tax dollars'
    elif profession == 'rapper':
        return 'Cristal'
    else:
        return 'Beer'