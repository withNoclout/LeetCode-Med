class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def max_consec(ch):
            left = 0
            count = 0
            res = 0
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    count += 1
                while count > k:
                    if answerKey[left] != ch:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1)
            return res

        return max(max_consec('T'), max_consec('F'))
