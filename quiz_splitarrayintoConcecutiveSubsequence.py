from collections import Counter, defaultdict

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)       # frequency of each number
        need = defaultdict(int)     # how many subsequences are waiting for this number

        for x in nums:
            if count[x] == 0:
                continue
            if need[x] > 0:
                # extend an existing subsequence
                need[x] -= 1
                need[x + 1] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                # create new subsequence x, x+1, x+2
                count[x + 1] -= 1
                count[x + 2] -= 1
                need[x + 3] += 1
            else:
                return False
            count[x] -= 1
        return True
