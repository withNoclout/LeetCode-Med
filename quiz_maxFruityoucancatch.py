class Solution : 
    def maxTotalFruits(self, fruits, startPos, k):
        left = 0 
        total = 0 
        res = 0 
        for right in range( len(fruits)  ) :
            total += fruits[right ][1] 

            while left <= right and self.minSteps(fruits[left][0] , fruits[right][0] , startPos ) > k  : 
                total -= fruits[left][1] 
                left += 1 

            res = max(res , total ) 

        return res
    
    def minSteps(self, left, right, startPos):
        goleft = abs(start - left ) + ( right - left ) 
        goRight = abs(start - right ) + ( right - left )
        return min(goleft, goRight) 
