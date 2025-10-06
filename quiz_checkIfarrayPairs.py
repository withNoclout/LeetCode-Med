class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        remainder_count = Counter([a % k for a in arr])

        for r in range(k):
            if r == 0:
                if remainder_count[r] % k != 0 and remainder_count[r] % 2 != 0:
                    return False
            elif 2 * r == k:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        return True
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        remainder_count = Counter([a % k for a in arr])

        for r in range(k):
            if r == 0:
                if remainder_count[r] % k != 0 and remainder_count[r] % 2 != 0:
                    return False
            elif 2 * r == k:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        return True
