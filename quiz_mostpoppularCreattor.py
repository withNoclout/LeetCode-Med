class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        total = {}
        best = {}
        
        for c, i, v in zip(creators, ids, views):
            total[c] = total.get(c, 0) + v
            if c not in best:
                best[c] = (v, i)
            else:
                curr_v, curr_i = best[c]
                if v > curr_v or (v == curr_v and i < curr_i):
                    best[c] = (v, i)
                    
        max_views = max(total.values())
        return [[c, best[c][1]] for c in total if total[c] == max_views]
