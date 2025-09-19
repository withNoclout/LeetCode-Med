class Solution:
	   def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        from collections import Counter
        def dfs(counter):
            total = 0
            for ch in counter:
                if counter[ch] > 0:
                    total += 1
                    counter[ch] -= 1
                    total += dfs(counter)
                    counter[ch] += 1
            return total
        return dfs(Counter(tiles))

