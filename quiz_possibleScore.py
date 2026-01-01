class Solution(object):
    def maxPossibleScore(self, start, d):
        """
        :type start: List[int]
        :type d: int
        :rtype: int
        """
        start.sort()
        n = len(start)
        
        def check(score):
            curr = start[0]
            for i in range(1, n):
                curr = max(curr + score, start[i])
                if curr > start[i] + d:
                    return False
            return True
            
        low, high = 0, 2000000000
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
