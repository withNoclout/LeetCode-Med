class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort( key =lambda x : x[1] )  

        curr_end = float('-inf')
        count = 0
        for start, end in pairs:
            if start > curr_end:
                count += 1
                curr_end = end
        return count
