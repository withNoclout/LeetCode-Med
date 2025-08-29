class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0  # count modifications

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                # Modify nums[i-1] if possible, else nums[i]
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]  # lower previous
                else:
                    nums[i] = nums[i - 1]  # raise current
        return True
