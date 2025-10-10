class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        b_count = 0
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                if b_count > 0:
                    deletions += 1
                    b_count -= 1
        return deletions
