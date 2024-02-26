def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    remaining_blue = blue_start - blue_pulled
    remaining_red = red_start - red_pulled
    total_remaining = remaining_blue + remaining_red

    probability_blue = remaining_blue / total_remaining
    return probability_blue
