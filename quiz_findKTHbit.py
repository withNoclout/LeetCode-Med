class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
            
        mid = 1 << (n - 1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # If it's in the second half, find its mirrored position in the first half
            # The length of the current string is (1 << n) - 1
            # Mirrored position of k is ((1 << n) - 1) - k + 1 = (1 << n) - k
            res = self.findKthBit(n - 1, (1 << n) - k)
            return "0" if res == "1" else "1"
