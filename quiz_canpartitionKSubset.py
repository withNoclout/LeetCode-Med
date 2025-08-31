class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if k <= 0 or total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        n = len(nums)
        memo = {}

        def dfs(used_mask, curr_sum, start_idx, buckets_left):
            if buckets_left == 1:  # last bucket will automatically fit
                return True
            if curr_sum == target:
                return dfs(used_mask, 0, 0, buckets_left - 1)
            key = (used_mask, curr_sum)
            if key in memo:
                return memo[key]

            prev = -1  # skip duplicates at same recursion layer
            for i in range(start_idx, n):
                if (used_mask >> i) & 1:
                    continue
                v = nums[i]
                if v == prev:
                    continue
                if curr_sum + v > target:
                    continue

                # choose
                next_mask = used_mask | (1 << i)
                if dfs(next_mask, curr_sum + v, i + 1, buckets_left):
                    memo[key] = True
                    return True

                prev = v
                if curr_sum == 0:  # prune: if first choice in bucket fails, no need to try others
                    break
                if curr_sum + v == target:  # prune: if filling to target fails, don't try others here
                    break

            memo[key] = False
            return False

        return dfs(0, 0, 0, k)
