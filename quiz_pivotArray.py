class Solution(object):
    def pivotArray(self, nums, pivot):
        less, equal, greater = [], [], []
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return less + equal + greater
