class Solution(object):
    def longestSubarray(self, nums):
        max_val = max(nums)

        # max_and will be the tastiest candy we found!
        max_and = max_val

        # Step 2: Find the longest stretch of the tastiest candy 📏
        max_len = 0         # Longest stretch we found so far (starts at 0)
        current_len = 0     # How long is the current candy stretch we're on?

        # Now, let's walk down the candy aisle... 🚶‍♀️
        for num in nums:
            if num == max_val:  # "Ooh, found another one of the tastiest candies!" 🎉
                current_len += 1  # The current stretch is getting longer!

                # "Is this stretch the longest we've seen yet?" 🤔
                max_len = max(max_len, current_len)  # Keeping track of the biggest candy party! 🥳
            else:
                current_len = 0  # "Aww, this candy is not the tastiest. Resetting the counter!" 😭

        return max_len
