class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(s):
            if len(s) == n:
                res.append(s)
                return
            
            dfs(s + "1")
            if not s or s[-1] == "1":
                dfs(s + "0")
                
        dfs("")
        return res
