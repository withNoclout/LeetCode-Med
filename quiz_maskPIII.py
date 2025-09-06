class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' in s:
            s = s.lower()
            local, domain = s.split('@')
            return local[0] + "*****" + local[-1] + "@" + domain
        # phone
        digits = [c for c in s if c.isdigit()]
        last4 = ''.join(digits[-4:])
        country = len(digits) - 10
        base = "***-***-" + last4
        if country > 0:
            return "+" + ("*" * country) + "-" + base
        return base
