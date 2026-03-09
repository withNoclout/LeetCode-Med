class Solution(object):
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                # Process the current group of three digits and append the unit (e.g., Million)
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
            
        return res.strip()

    def helper(self, num):
        # Base cases for recursion based on standard English naming rules
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            # Handle the hundreds place and recurse for the rest
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)
