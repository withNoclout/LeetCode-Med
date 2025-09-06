class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0
        up = down = ans = 0
        for i in range(1, n):
            if (down > 0 and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                up = down = 0
            if arr[i] > arr[i-1]:
                up += 1
            elif arr[i] < arr[i-1]:
                if up > 0:
                    down += 1
                    ans = max(ans, up + down + 1)
        return ans
