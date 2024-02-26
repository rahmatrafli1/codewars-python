def cannons_ready(gunners):
    return "Fire!" if all(gunners[gunner] == 'aye' for gunner in gunners) else "Shiver me timbers!"