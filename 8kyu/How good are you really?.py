def better_than_average(class_points, your_points):
    # Your code here
    # Calculate the average of class points
    class_average = sum(class_points) / len(class_points)
    
    # Compare your points to the average
    return your_points > class_average