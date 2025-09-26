class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        prefix = [0]
        for x in arr:
            prefix.append(prefix[-1] + x)

        res, diff = 0, float('inf')
        for v in range(1, max(arr) + 1):
            # find index of first element > v
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if arr[mid] > v:
                    r = mid
                else:
                    l = mid + 1
            total = prefix[l] + (n - l) * v
            cur_diff = abs(total - target)
            if cur_diff < diff:
                diff = cur_diff
                res = v
        return res
