class Solution(object):
    def minimumOperations(self, num):
        n = len(num)
        found_0 = False
        found_5 = False
        
        for i in range(n - 1, -1, -1):
            c = num[i]
            if found_0 and (c == '0' or c == '5'):
                return n - i - 2
            if found_5 and (c == '2' or c == '7'):
                return n - i - 2
            
            if c == '0': found_0 = True
            if c == '5': found_5 = True
            
        return n - 1 if found_0 else n
