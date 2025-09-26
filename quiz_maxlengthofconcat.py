class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # filter out strings with duplicate chars
        arr = [s for s in arr if len(set(s)) == len(s)]
        
        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append((mask, len(s)))

        self.ans = 0

        def dfs(i, cur_mask, cur_len):
            self.ans = max(self.ans, cur_len)
            for j in range(i, len(masks)):
                m, l = masks[j]
                if cur_mask & m == 0:  # no overlap
                    dfs(j + 1, cur_mask | m, cur_len + l)

        dfs(0, 0, 0)
        return self.ans
