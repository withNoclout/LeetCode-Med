# ...existing code...
class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        seen = set()
        for w in words:
            even = [0] * 26
            odd = [0] * 26
            for i, ch in enumerate(w):
                if i % 2 == 0:
                    even[ord(ch) - 97] += 1
                else:
                    odd[ord(ch) - 97] += 1
            seen.add((tuple(even), tuple(odd)))
        return len(seen)
#
