class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))

        # Build maximum number by replacing the first non-9 digit with 9
        s_max = s[:]
        for ch in s_max:
            if ch != '9':
                target = ch
                s_max = [c if c != target else '9' for c in s_max]
                break
        max_num = int("".join(s_max))

        # Build minimum number
        s_min = s[:]
        if s_min[0] != '1':
            target = s_min[0]
            s_min = [c if c != target else '1' for c in s_min]
        else:
            for ch in s_min[1:]:
                if ch != '0' and ch != '1':
                    target = ch
                    s_min = [c if c != target else '0' for c in s_min]
                    break
        min_num = int("".join(s_min))

        return max_num - min_num
