def how_much_i_love_you(nb_petals):
    # your code
    pharses = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return pharses[(nb_petals - 1) % len(pharses)]