class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev = 0
        result = 0
        for row in bank:
            devices = row.count('1')
            if devices:
                result += prev * devices
                prev = devices
        return result
