class Solution(object):
    def maxPoints(self, technique1, technique2, k):
        """
        :type technique1: List[int]
        :type technique2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(technique1)
        total_points = 0
        count1 = 0
        diffs = []
        
        for i in range(n):
            if technique1[i] >= technique2[i]:
                # Technique 1 is better or equal, so we pick it naturally.
                total_points += technique1[i]
                count1 += 1
            else:
                # Technique 2 is better, pick it for now.
                total_points += technique2[i]
                # Record the cost if we are forced to switch this back to Technique 1 later.
                # Cost = (Points we lose) = Tech2 - Tech1
                diffs.append(technique2[i] - technique1[i])
                
        # If we haven't met the quota for Technique 1
        if count1 < k:
            needed = k - count1
            # Sort the costs (diffs) to find the cheapest switches
            diffs.sort()
            
            # Subtract the smallest costs to satisfy the requirement
            for i in range(needed):
                total_points -= diffs[i]
                
        return total_points
