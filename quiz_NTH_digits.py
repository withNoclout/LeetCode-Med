class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length, count, start = 1, 9, 1
        
        # Find the range where the nth digit is located
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Find the actual number containing the nth digit
        num = start + (n - 1) // length
        digit_index = (n - 1) % length
        
        return int(str(num)[digit_index])
