class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        # Greedy fact: after applying operations optimally, the string becomes all '1's
        # except possibly one '0'. If there are z zeros and the first zero is at index f,
        # the single '0' (if any) ends up at position f + z - 1.
        n = len(binary)
        z = binary.count('0')
        if z <= 1:
            return binary

        f = binary.find('0')
        res = ['1'] * n
        res[f + z - 1] = '0'
        return ''.join(res)
