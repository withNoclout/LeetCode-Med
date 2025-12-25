class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        n = len(nums)
        total_sum = sum(nums)
        marked = [False] * n
        # Sort by value, then by index
        sorted_nums = sorted((val, i) for i, val in enumerate(nums))
        ptr = 0
        res = []
        
        for idx, k in queries:
            # Part 1: Mark the specific index
            if not marked[idx]:
                marked[idx] = True
                total_sum -= nums[idx]
            
            # Part 2: Mark k smallest unmarked elements
            while k > 0 and ptr < n:
                val, i = sorted_nums[ptr]
                if not marked[i]:
                    marked[i] = True
                    total_sum -= val
                    k -= 1
                ptr += 1
            
            res.append(total_sum)
            
        return res


class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
