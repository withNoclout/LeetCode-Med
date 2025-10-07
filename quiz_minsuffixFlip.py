class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips = 0
        curr = '0'
        for ch in target:
            if ch != curr:
                flips += 1
                curr = ch
        return flips
