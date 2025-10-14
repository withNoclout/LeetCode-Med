class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre_even = [0] * n
        pre_odd = [0] * n

        # prefix sums by parity
        for i, v in enumerate(nums):
            if i == 0:
                if i % 2 == 0:
                    pre_even[i] = v
                else:
                    pre_odd[i] = v
            else:
                pre_even[i] = pre_even[i-1]
                pre_odd[i] = pre_odd[i-1]
                if i % 2 == 0:
                    pre_even[i] += v
                else:
                    pre_odd[i] += v

        total_even = pre_even[-1]
        total_odd = pre_odd[-1]

        ans = 0
        for i, v in enumerate(nums):
            left_even = pre_even[i-1] if i > 0 else 0
            left_odd = pre_odd[i-1] if i > 0 else 0

            # sums on the right side before removal (original parity)
            right_even = total_even - pre_even[i]
            right_odd = total_odd - pre_odd[i]

            # after removing nums[i], right side shifts parity
            new_even = left_even + right_odd
            new_odd = left_odd + right_even

            if new_even == new_odd:
                ans += 1

        return ans
