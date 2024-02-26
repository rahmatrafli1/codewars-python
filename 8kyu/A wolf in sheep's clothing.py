def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        index_of_wolf = queue.index("wolf")
        return f"Oi! Sheep number {len(queue) - index_of_wolf - 1}! You are about to be eaten by a wolf!"