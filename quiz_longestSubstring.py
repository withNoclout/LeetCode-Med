class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state = 0
        seen = {0: -1}  # state -> earliest index
        res = 0

        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                state ^= vowel_to_bit[ch]  # flip the bit for this vowel
            if state in seen:
                res = max(res, i - seen[state])
            else:
                seen[state] = i

        return res
