class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # We need the count of unique values of (n1 ^ n2 ^ n3)
        # Deduplicate to speed up iteration
        distinct = list(set(nums))
        
        # Max value is 1500, so XOR results will be < 2048 (2^11)
        limit = 2048
        
        # 1. Calculate all unique pair XORs
        # Using a boolean array is faster than a set for dense ranges in Python
        seen_pairs = [False] * limit
        for a in distinct:
            for b in distinct:
                seen_pairs[a ^ b] = True
        
        # 2. Calculate all unique triplet XORs (pair ^ third)
        seen_triplets = [False] * limit
        
        # Optimization: Only iterate over pairs that actually exist
        valid_pairs = [val for val, exists in enumerate(seen_pairs) if exists]
        
        for p in valid_pairs:
            for c in distinct:
                seen_triplets[p ^ c] = True
                
        return sum(seen_triplets)
