class Solution(object):
    def subArrayRanges(self, nums):
        n = len(nums)
        # contribution as maximum
        max_sum = 0
        st = []
        for i in range(n + 1):
            cur = float('inf') if i == n else nums[i]
            while st and (i == n or nums[st[-1]] <= cur):
                j = st.pop()
                k = st[-1] if st else -1
                max_sum += nums[j] * (j - k) * (i - j)
            st.append(i)

        # contribution as minimum
        min_sum = 0
        st = []
        for i in range(n + 1):
            cur = float('-inf') if i == n else nums[i]
            while st and (i == n or nums[st[-1]] >= cur):
                j = st.pop()
                k = st[-1] if st else -1
                min_sum += nums[j] * (j - k) * (i - j)
            st.append(i)

        return max_sum - min_sum
