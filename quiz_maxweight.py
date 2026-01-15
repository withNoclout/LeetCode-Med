class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        pizzas.sort(reverse=True)
        n = len(pizzas)
        days = n // 4
        odd_days = (days + 1) // 2
        even_days = days // 2
        
        # Pick the largest pizzas for the odd days
        total_weight = sum(pizzas[:odd_days])
        
        # For even days, skip 1 (the largest in the group) and pick the next (2nd largest)
        curr = odd_days
        for _ in range(even_days):
            curr += 1
            total_weight += pizzas[curr]
            curr += 1
            
        return total_weight
