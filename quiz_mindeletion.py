class Solution(object):
    def minDeletionSize(self, strs):
        res = 0
        n = len(strs)
        # Tracks if strs[i] < strs[i+1] is already satisfied by previous columns
        is_sorted = [False] * (n - 1)
        
        for j in range(len(strs[0])):
            # If any pair is not yet sorted and this column violates order, delete column
            if any(not is_sorted[i] and strs[i][j] > strs[i+1][j] for i in range(n - 1)):
                res += 1
            else:
                # Keep column: update sorted status where strict inequality occurs
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
                        
        return resfrom collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s).values()
        used = set()
        deletions = 0
        for f in freq:
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            if f > 0:
                used.add(f)
        return deletions
