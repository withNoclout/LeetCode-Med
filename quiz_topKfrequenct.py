class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        freq = Counter(nums )
        bucket = [ [] for _ in range(len(nums) + 1 ) ] 

        for num , f in freq.items():
            bucket[f].append(num)
        ans = [] 
        for f in range(len(bucket) - 1, 0, -1):
            for num in bucket[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans
