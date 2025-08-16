class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        remaining = 0
        for byte in data:
            byte &= 0xFF  # only keep last 8 bits
            
            if remaining == 0:
                if (byte >> 7) == 0:  # 1-byte char: 0xxxxxxx
                    continue
                elif (byte >> 5) == 0b110:  # 2-byte char: 110xxxxx
                    remaining = 1
                elif (byte >> 4) == 0b1110:  # 3-byte char: 1110xxxx
                    remaining = 2
                elif (byte >> 3) == 0b11110:  # 4-byte char: 11110xxx
                    remaining = 3
                else:
                    return False
            else:
                # continuation byte must start with "10"
                if (byte >> 6) != 0b10:
                    return False
                remaining -= 1
        
        return remaining == 0
