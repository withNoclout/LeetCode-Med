class Solution(object):
    def findMaxLength(self, nums):
        count_to_index = {0: -1}  # balance -> first index
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_to_index:
                max_len = max(max_len, i - count_to_index[count])
            else:
                count_to_index[count] = i

        return max_len
