from collections import Counter

class Solution(object):
    def minimumOperations(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        even = Counter(nums[::2])
        odd = Counter(nums[1::2])

        e_top = even.most_common(2) + [(None, 0)] * 2
        o_top = odd.most_common(2) + [(None, 0)] * 2

        (e1v, e1c), (e2v, e2c) = e_top[0], e_top[1]
        (o1v, o1c), (o2v, o2c) = o_top[0], o_top[1]

        if e1v != o1v:
            keep = e1c + o1c
        else:
            keep = max(e1c + o2c, e2c + o1c)

        return n - keep
