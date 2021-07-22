def trapRainWater(height):
    
    # initiate variables
    l = l_max = r_max = water = 0
    r = len(height) - 1
    
    while l < r:
        if (left := height[l]) < (right := height[r]):
            if l_max < left:
                l_max = left
            else:
                water += l_max - left
            l += 1
         else:
            if r_max < right:
                r_max = right
            else:
                water += r_max - right
            r -= 1
    return water    
            
    
