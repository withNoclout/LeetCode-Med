class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        num = list(num)
        started = False

        for i in range(len(num)):
            d = int(num[i])
            if change[d] > d:
                num[i] = str(change[d])
                started = True
            elif change[d] == d and started:
                num[i] = str(change[d])
            elif started:
                break

        return ''.join(num)
