class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        for i in range(0, len(s), k):
            current_sum = 0
            for char in s[i : i+k]:
                current_sum += ord(char) - ord('a')
            hashed_char = chr((current_sum % 26) + ord('a'))
            res.append(hashed_char)
            
        return "".join(res)
