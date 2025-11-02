from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old = self.nums2[index]
        self.count2[old] -= 1
        if self.count2[old] == 0:
            del self.count2[old]
        self.nums2[index] += val
        self.count2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res = 0
        for x in self.nums1:
            res += self.count2.get(tot - x, 0)
        return res
