class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2** 31 and divisor == -1 : 
            return 2**31 - 1 
        
        negative = ( dividend < 0 ) != ( divisor < 0  ) 

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0 

        while dividend >= divisor :
            temp_divisor  = divisor
            num_divisors = 1
            while dividend >= ( temp_divisor << 1 ) :
                temp_divisor <<= 1 
                num_divisors <<= 1 

            dividend -=  temp_divisor 
            quotient += num_divisors 

        return -quotient if negative else quotient
