class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        arr = colors + colors[:k-1]
        ans = 0
        cnt = 1
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                cnt += 1
            else:
                cnt = 1
                
            if cnt >= k:
                ans += 1
                
        return ans
