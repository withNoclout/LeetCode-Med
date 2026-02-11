class Solution(object):
    def maxSumOfSquares(self, num, total_sum):
        """
        :type num: int
        :type total_sum: int
        :rtype: str
        """
        # If the sum is greater than the maximum possible sum (all 9s), return empty
        if total_sum > 9 * num:
            return ""
            
        res = []
        current_sum = total_sum
        
        for _ in range(num):
            # Greedily pick the largest digit possible (max 9)
            d = min(9, current_sum)
            res.append(str(d))
            current_sum -= d
            
        # If we haven't exactly used up the sum (e.g. if sum was initially negative), return empty
        if current_sum != 0:
            return ""
            
        return "".join(res)
