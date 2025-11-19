class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        total = sum(diffs)
        if total <= k:
            return 0

        diffs.sort(reverse=True)
        diffs.append(0)
        n = len(diffs)

        for i in range(n - 1):
            cnt = i + 1
            diff = diffs[i] - diffs[i + 1]
            need = cnt * diff
            if need <= k:
                k -= need
            else:
                dec = k // cnt
                rem = k % cnt
                level = diffs[i] - dec
                ans = 0
                for j in range(cnt):
                    val = level - (1 if j < rem else 0)
                    ans += val * val
                for j in range(cnt, n - 1):
                    ans += diffs[j] * diffs[j]
                return ans

        ans = 0
        for i in range(n - 1):
            ans += diffs[i] * diffs[i]
        return ans
