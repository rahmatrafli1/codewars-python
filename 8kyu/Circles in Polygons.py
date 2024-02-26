import math

def circle_diameter(sides, side_length): 
    # your code here
    if sides < 3 or side_length <= 0:
        return "Invalid input"
    
    diameter = side_length / math.tan(math.pi / sides)
    return round(diameter, 10)