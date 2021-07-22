def trapRainWater(height):
    
    # initiate variables
    l = l_max = r_max = water = 0
    r = len(height) - 1
    
    while l < r:
        if (left := height[l]) < (right := height[r]): # manipulate smaller side
            if l_max < left: # update side max
                l_max = left
            else:
                water += l_max - left # add water 
            l += 1
        else:
            if r_max < right:
                r_max = right
            else:
                water += r_max - right
            r -= 1
    return water    
            
    
