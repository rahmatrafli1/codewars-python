import math

def ice_brick_volume(radius, bottle_length, rim_length):
    # Ensure the parameters are positive and valid
    if radius > 0 and bottle_length > 0 and rim_length >= 0 and rim_length < bottle_length:
        # Calculate the volume of the ice brick
        volume = 2 * radius**2 * (bottle_length - rim_length)
        return round(volume, 2)  # Round the result to two decimal places
    else:
        return "Invalid parameters"