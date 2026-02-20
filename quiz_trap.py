class Solution(object):
    def trap(self, height):
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0
        
        while left < right:
            # The smaller max height dictates how much water can be trapped
            if left_max < right_max:
                left += 1
                # Update max before calculating to avoid negative water
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                
        return trapped_water
