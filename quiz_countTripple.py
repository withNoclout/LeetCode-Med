class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        res = 0
        for i in range(n):
            for k in range(i+1, n):
                if prefix[i] == prefix[k+1]:
                    res += (k - i)
        return res
