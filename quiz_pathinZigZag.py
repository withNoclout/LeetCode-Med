class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label:
            res.append(label)
            level = label.bit_length()
            # Find the parent in the zigzag tree
            label = (1 << (level - 1)) + (1 << level) - 1 - label
            label //= 2
        return res[::-1]
