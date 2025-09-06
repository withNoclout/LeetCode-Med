class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        for i, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            if s[i:i+len(src)] == src:
                s = s[:i] + tgt + s[i+len(src):]
        return s
