class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen = set()
        n = len(nums)

        for i in range(n):
            div_cnt = 0
            cur = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    div_cnt += 1
                    if div_cnt > k:
                        break
                cur.append(nums[j])
                seen.add(tuple(cur))

        return len(seen)
