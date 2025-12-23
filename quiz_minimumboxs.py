class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        res = 0
        for c in capacity:
            if total_apples <= 0:
                break
            total_apples -= c
            res += 1
            
        return res
