class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # Calculate how many items satisfy BOTH requirements simultaneously
        overlap = min(need1, need2)
        
        # Calculate remaining needs after the overlap is satisfied
        rem1 = need1 - overlap
        rem2 = need2 - overlap
        
        # 1. Cost for the overlapping part:
        # We can either buy separate items (cost1 + cost2) or one shared item (costBoth).
        cost_overlap = overlap * min(cost1 + cost2, costBoth)
        
        # 2. Cost for the remaining Type 1 needs:
        # We can buy Type 1 specifically, or buy 'Both' (and waste the Type 2 part).
        cost_rem1 = rem1 * min(cost1, costBoth)
        
        # 3. Cost for the remaining Type 2 needs:
        # We can buy Type 2 specifically, or buy 'Both' (and waste the Type 1 part).
        cost_rem2 = rem2 * min(cost2, costBoth)
        
        return cost_overlap + cost_rem1 + cost_rem2class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int min1 = 100; 
        int min2 = 100;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] < min1){
                min2 = min1;
                min1 = nums[i];
            }
            else if(nums[i] < min2){
                min2 = nums[i];
            }
        }
        return nums[0] + min1 + min2;
    }
};
