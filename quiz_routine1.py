class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cnt = [0] * 26
        for c in word2:
            cnt[ord(c) - ord('a')] += 1
            
        missing = len(word2)
        ans = 0
        left = 0
        n = len(word1)
        
        for right, char in enumerate(word1):
            idx = ord(char) - ord('a')
            if cnt[idx] > 0:
                missing -= 1
            cnt[idx] -= 1
            
            while missing == 0:
                ans += n - right
                left_idx = ord(word1[left]) - ord('a')
                cnt[left_idx] += 1
                if cnt[left_idx] > 0:
                    missing += 1
                left += 1
                
        return ans
