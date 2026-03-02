class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return [""]
            
            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in word_set:
                    sub_sentences = dfs(j)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            
            memo[i] = res
            return res

        return dfs(0)
