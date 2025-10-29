class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        res = [0] * n
        count = moves = 0
        for i in range(n):
            res[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        count = moves = 0
        for i in range(n - 1, -1, -1):
            res[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        return res
