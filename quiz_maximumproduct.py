class Solution : 
    def maximumProduct(self , nums, m):
        n = len(nums)
        ans = float('-inf')

        if m == 1:
            for x in nums:
                ans = max(ans, x * x)
            return ans

        maxi = float('-inf')
        mini = float('inf')

        for j in range(m - 1, n):
            i = j - m + 1
            maxi = max(maxi, nums[i])
            mini = min(mini, nums[i])

            prod1 = maxi * nums[j]
            prod2 = mini * nums[j]
            ans = max(ans, max(prod1, prod2))

        return ans
