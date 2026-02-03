class Solution(object):
    def maxBalancedShipments(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        ans = 0
        mx = 0
        
        for w in weight:
            # Update the maximum weight seen in the current potential shipment
            mx = max(mx, w)
            
            # If the current weight is strictly less than the max, 
            # we found a balanced shipment ending here.
            # Greedily close it to maximize the total count.
            if w < mx:
                ans += 1
                mx = 0  # Reset max to start a new shipment
                
        return ans
