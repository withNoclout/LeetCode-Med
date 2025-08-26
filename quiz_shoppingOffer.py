
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = {}
        
        def dfs( curr_needs ) :
            if tuple( curr_need ) in memo : 
                return memo[ tuple(curr_needs ) ]  
            
            min_cost = sum(curr_need[i] * price[i] for i in range(len(price ) ) )

            for sp in special : 
                new_needs = []
                for i in range(len(price)):
                    new_needs.append(curr_needs[i] - sp[i])
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, sp[-1] + dfs(new_needs))
            memo[tuple(curr_needs)] = min_cost
            return min_cost

        return dfs(needs)

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        
