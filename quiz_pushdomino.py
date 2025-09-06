class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        s = "L" + dominoes + "R"
        res = []
        prev = 0
        for i in range(1, len(s)):
            if s[i] == '.':
                continue
            middle = i - prev - 1
            if s[prev] == s[i]:
                # all fall the same way
                res.append(s[i] * (middle + 1))  # includes the left endpoint char at position prev+1..i
            elif s[prev] == 'L' and s[i] == 'R':
                # dots remain upright
                res.append('L')  # for position prev+1? adjust below
                res[-1] = ''  # remove; we'll handle endpoints uniformly after loop
                res.append('L' * 0)  # no-op to keep logic simple
                res.append('.' * middle)
                res.append('R')  # will be handled in next segment
            else:  # 'R' ... 'L'
                left = middle // 2
                right = middle // 2
                mid = '' if middle % 2 == 0 else '.'
                res.append('R' + 'R' * left + mid + 'L' * right)
            prev = i

        # rebuild properly without the sentinel logic confusion
        # redo with a clean pass:
        s = "L" + dominoes + "R"
        ans = []
        prev = 0
        for i in range(1, len(s)):
            if s[i] == '.':
                continue
            middle = i - prev - 1
            if prev > 0:  # append the actual previous force char (not the left sentinel)
                ans.append(s[prev])
            if s[prev] == s[i]:
                ans.append(s[i] * middle)
            elif s[prev] == 'L' and s[i] == 'R':
                ans.append('.' * middle)
            else:  # 'R' ... 'L'
                left = middle // 2
                right = middle // 2
                mid = '' if middle % 2 == 0 else '.'
                ans.append('R' * left + mid + 'L' * right)
            prev = i
        # skip the trailing sentinel 'R' and leading sentinel 'L'
        return ''.join(ans)

