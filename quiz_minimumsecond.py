class Solution(object):
    def minimumSeconds(self, nums):
        import collections
        n = len(nums)
        positions = collections.defaultdict(list)
        
        for i, x in enumerate(nums):
            positions[x].append(i)
            
        res = n
        
        for pos in positions.values():
            # Append the first index + n to handle the circular gap easily
            pos.append(pos[0] + n)
            
            max_dist = 0
            for i in range(len(pos) - 1):
                max_dist = max(max_dist, pos[i+1] - pos[i])
            
            # The time needed is floor(max_distance / 2)
            res = min(res, max_dist // 2)
            
        return res
