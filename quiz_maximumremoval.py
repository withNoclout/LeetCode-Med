class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def is_subsequence(removed_set):
            j = 0
            for i, ch in enumerate(s):
                if i in removed_set:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return j == len(p)

        left, right = 0, len(removable)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            removed_set = set(removable[:mid])
            if is_subsequence(removed_set):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
