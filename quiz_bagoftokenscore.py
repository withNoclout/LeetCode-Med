class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        score = res = 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return res
