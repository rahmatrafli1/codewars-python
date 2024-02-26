def get_size(w,h,d):
    #your code here
    volume = w * h * d
    
    return [2 * (w * h + h * d + d * w), volume]