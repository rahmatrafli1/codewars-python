def find_slope(points):
    # Check if the input list has exactly four elements
    if len(points) != 4:
        return "undefined"
    
    # Extract coordinates of the two points
    x1, y1, x2, y2 = points

    # Check if the line is vertical (undefined slope)
    if x1 == x2:
        return "undefined"

    # Calculate the slope
    slope = (y2 - y1) // (x2 - x1)

    return str(slope)
