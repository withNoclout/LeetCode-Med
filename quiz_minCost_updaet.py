class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        # Calculate the total cost of deleting everything
        total_sum = sum(cost)
        
        # Dictionary to store the sum of costs for each unique character
        # char_savings[char] = sum of costs for all occurrences of 'char'
        char_savings = {}
        
        for i, char in enumerate(s):
            char_savings[char] = char_savings.get(char, 0) + cost[i]
            
        # To minimize deletion cost, we must maximize the cost of the characters we KEEP.
        # We find the character that has the highest total cost and keep all instances of it.
        max_saved = 0
        for char in char_savings:
            if char_savings[char] > max_saved:
                max_saved = char_savings[char]
                
        # Min Cost = Total Cost - Max Savings
        return total_sum - max_saved
