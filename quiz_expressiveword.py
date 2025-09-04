class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def stretchy(w):
            i = j = 0
            n, m = len(s), len(w)
            while i < n and j < m:
                if s[i] != w[j]:
                    return False
                # count run in s
                i0 = i
                while i < n and s[i] == s[i0]:
                    i += 1
                a = i - i0
                # count run in w
                j0 = j
                while j < m and w[j] == w[j0]:
                    j += 1
                b = j - j0
                # valid if same count or s-run stretched (>=3) and b <= a
                if not (a == b or (a >= 3 and b <= a and b >= 1)):
                    return False
            return i == n and j == m

        ans = 0
        for w in words:
            if stretchy(w):
                ans += 1
        return ans
