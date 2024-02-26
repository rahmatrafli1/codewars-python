def duck_duck_goose(players, goose):
    goose_index = (goose - 1) % len(players)
    return players[goose_index].name