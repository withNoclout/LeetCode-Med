class Solution(object):
    def subarrayBitwiseORs(self, arr):
        result = set()
        curr = set()
        
        for num in arr:
            curr = {num | x for x in curr} | {num}
            result |= curr
        
        return len(result)

