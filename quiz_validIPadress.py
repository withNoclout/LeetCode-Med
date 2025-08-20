class Solution(object):
    def validIPAddress(self, queryIP):
        if self.isIPv4(queryIP):
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"

    def isIPv4(self, ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if len(part) > 1 and part[0] == "0":  # leading zeros
                return False
            if not 0 <= int(part) <= 255:
                return False
        return True

    def isIPv6(self, ip):
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        hex_digits = "0123456789abcdefABCDEF"
        for part in parts:
            if not (1 <= len(part) <= 4):
                return False
            if not all(c in hex_digits for c in part):
                return False
        return True
