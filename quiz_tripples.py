class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from collections import Counter
        def count(a, b):
            res = 0
            cnt = Counter()
            for x in b:
                cnt[x] += 1
            for x in a:
                target = x * x
                for y in b:
                    if target % y == 0:
                        z = target // y
                        if z in cnt:
                            res += cnt[z]
                cnt = Counter()
                for y in b:
                    cnt[y] += 1
            return res // 2

        def count_pairs(a, b):
            res = 0
            cnt = Counter(b)
            for x in a:
                target = x * x
                seen = Counter()
                for y in b:
                    if target % y == 0:
                        z = target // y
                        if z in seen:
                            res += seen[z]
                    seen[y] += 1
            return res

        def helper(a, b):
            res = 0
            n = len(b)
            for x in a:
                target = x * x
                seen = Counter()
                for y in b:
                    if target % y == 0:
                        z = target // y
                        res += seen[z]
                    seen[y] += 1
            return res

        return helper(nums1, nums2) + helper(nums2, nums1)
