class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        res = []
        for i, j in zip(l, r):
            arr = nums[i:j+1]
            m = len(arr)
            mn, mx = min(arr), max(arr)
            if m <= 2 or mn == mx:
                res.append(True)
                continue
            diff_total = mx - mn
            if diff_total % (m - 1) != 0:
                res.append(False)
                continue
            d = diff_total // (m - 1)
            if d == 0:
                res.append(False)
                continue
            seen = set()
            ok = True
            for v in arr:
                dv = v - mn
                if dv % d != 0:
                    ok = False
                    break
                k = dv // d
                if k in seen:
                    ok = False
                    break
                seen.add(k)
            res.append(ok and len(seen) == m)
        return res

