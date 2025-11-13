class Solution(object):
    def sumOfThree(self, num):
        if num % 3 != 0:
            return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]

