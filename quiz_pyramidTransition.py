import collections

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        adj = collections.defaultdict(list)
        for s in allowed:
            adj[s[:2]].append(s[2])
            
        memo = {}

        def dfs(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]
            
            def build_next(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)
                
                key = row[i:i+2]
                for char in adj[key]:
                    if build_next(i + 1, next_row + char):
                        return True
                return False
            
            memo[row] = build_next(0, "")
            return memo[row]
            
        return dfs(bottom)
