def combat(health, damage):
    #your code here
    remaining_health = health - damage
    return max(remaining_health, 0)