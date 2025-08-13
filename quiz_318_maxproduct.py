class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = []
        lens = [] 
        for w in words : 
            m = 0 
            for ch in set(w) :
                m |= 1 << ( ord(ch ) - 97 ) 
            masks.append(m) 
            lens.append(len(w) ) 

        ans = 0 
        n = len(words ) 
        for i in range(n) :
            for j in range(i + 1 , n) :
                if masks[i] & masks[j] == 0 :
                    prod = lens[i] * lens[j] 
                    if prod > ans : 
                        ans  = prod 
        return ans  
