class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums  )
        pref = [0 ] * ( n + 1 )   
        for i in range(n ) : 
            pref[i+1 ] = pref[i] + nums[i] 

        res = [0] * n 
        total = pref[n] 

        for i in range(n) :
            left = x * i - pref[i] 
            right = ( total - pref[i+1 ] ) -x  * ( n - i - 1 ) 
            res[i] = left + right 

        return res    
