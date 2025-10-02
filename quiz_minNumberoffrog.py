class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        seq = "croak"
        count = {ch: 0 for ch in seq}
        frogs, max_frogs = 0, 0

        for ch in croakOfFrogs:
            if ch == 'c':
                count['c'] += 1
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            elif ch == 'r':
                if count['c'] == 0: return -1
                count['c'] -= 1
                count['r'] += 1
            elif ch == 'o':
                if count['r'] == 0: return -1
                count['r'] -= 1
                count['o'] += 1
            elif ch == 'a':
                if count['o'] == 0: return -1
                count['o'] -= 1
                count['a'] += 1
            elif ch == 'k':
                if count['a'] == 0: return -1
                count['a'] -= 1
                frogs -= 1
            else:
                return -1  # invalid character

        # After processing, all counts should be zero
        if any(count[ch] != 0 for ch in "croa"):
            return -1

        return max_frogs
