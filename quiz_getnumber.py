class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ["+", "-"]:
                # A sign is only valid at the start or immediately after an exponent
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
                    
            elif char == ".":
                # A dot is only valid if we haven't seen one yet, AND we aren't in the exponent part
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            elif char in ["e", "E"]:
                # An exponent is only valid if we haven't seen one yet, AND we've seen a digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because we MUST have digits after the exponent
                seen_digit = False
                
            else:
                # Any other character (letters, spaces, etc.) makes it invalid
                return False
                
        # If we end the string and haven't seen a digit (or reset it after an 'e'), it's invalid
        return seen_digit
