class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the numbers by their absolute values in descending order.
        # This brings the elements with the largest magnitudes to the front.
        nums.sort(key=abs, reverse=True)
        
        # Pick the two numbers with the largest absolute values.
        # We multiply them, take the absolute value (to handle negative * negative or positive * positive),
        # and then multiply by the maximum replacement magnitude (100,000).
        max_pair_product = abs(nums[0] * nums[1])
        
        return max_pair_product * 100000
